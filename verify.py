"""Verify saved aggregate snapshots using Python 3's standard library."""
import csv
import hashlib
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

root = Path(__file__).resolve().parent
for entry in (root / 'SHA256SUMS.txt').read_text(encoding='ascii').splitlines():
    digest, name = entry.split('  ', 1)
    path = (root / name).resolve()
    assert path.is_relative_to(root), 'Checksum path outside this publication'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, name

def rows(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))

for path in sorted((root / 'snapshots').glob('*/snapshot.json')):
    data = json.loads(path.read_text(encoding='utf-8'))
    asof = datetime.fromisoformat(data['as_of_utc'])
    start = datetime.fromisoformat(data['window_start_utc'])
    assert asof.utcoffset() == timedelta(0) and asof - start == timedelta(days=7)
    assert data['as_of_utc'] == data['window_end_utc']
    assert data['window_boundary'] == 'inclusive'
    assert path.parent.name == asof.strftime('%Y-%m-%dT%H%M%SZ')
    count_fields = [key for key, value in data.items() if isinstance(value, int)]
    assert all(type(data[key]) is int and data[key] >= 0 for key in count_fields)
    assert data['total_stored_notice_records'] == sum(data[key] for key in (
        'future_deadline_notice_records', 'past_or_equal_deadline_notice_records',
        'unusable_or_missing_deadline_notice_records'))
    assert data['first_imported_last_seven_days'] <= data['total_stored_notice_records']
    assert sum(row['first_imported_last_seven_days'] for row in data['sources']) == data['first_imported_last_seven_days']

    files = [('source-imports.csv', 'sources'),
             ('future-deadline-by-region.csv', 'regions'),
             ('future-deadline-by-cpv-division.csv', 'cpv_divisions')]
    for filename, key in files:
        actual = rows(path.parent / filename)
        expected = [{key: '' if value is None else str(value) for key, value in row.items()}
                    for row in data[key]]
        assert actual == expected, filename

    assert len(data['regions']) == 12
    assert len({row['region_code'] for row in data['regions']}) == 12
    for row in data['regions']:
        assert re.fullmatch('UK[C-N]', row['region_code'])
        assert 0 <= row['notice_records'] <= data['future_deadline_notice_records']
    assert len({row['cpv_division_code'] for row in data['cpv_divisions']}) == len(data['cpv_divisions'])
    for row in data['cpv_divisions']:
        assert re.fullmatch('[0-9]{2}', row['cpv_division_code'])
        assert 0 < row['notice_records'] <= data['future_deadline_notice_records']
    for row in data['sources']:
        assert type(row['first_imported_last_seven_days']) is int
        assert row['first_imported_last_seven_days'] >= 0
        if row['feed_last_checked_utc']:
            checked = datetime.fromisoformat(row['feed_last_checked_utc'])
            assert checked.utcoffset() == timedelta(0) and checked <= asof
    assert 0 <= data['future_deadline_records_without_known_region'] <= data['future_deadline_notice_records']
    assert 0 <= data['future_deadline_records_without_known_cpv_division'] <= data['future_deadline_notice_records']
    print('PASS:', path.parent.name, '- checksums, timestamps, CSV/JSON agreement, count relationships and code formats')
