"""Verify the saved trade publication using Python's standard library."""
import csv, hashlib, json, re
from datetime import datetime, timedelta
from pathlib import Path

root=Path(__file__).resolve().parent
for line in (root/'SHA256SUMS.txt').read_text(encoding='ascii').splitlines():
    expected,name=line.split('  ',1)
    path=(root/name).resolve()
    assert path.is_relative_to(root) and hashlib.sha256(path.read_bytes()).hexdigest()==expected,name

def read_csv(path):
    with path.open(encoding='utf-8',newline='') as stream:return list(csv.DictReader(stream))

paths=list((root/'trade-snapshots').glob('*/trade-snapshot.json'))
assert paths
for path in paths:
    data=json.loads(path.read_text(encoding='utf-8'))
    assert data['schema_version']=='trade-1.0'
    instant=datetime.fromisoformat(data['as_of_utc'])
    assert instant.utcoffset()==timedelta(0) and path.parent.name==instant.strftime('%Y%m%dT%H%M%SZ')
    assert sum(data[k] for k in ('inactive_records','active_unusable_deadline_records','active_past_or_equal_deadline_records','active_future_deadline_records'))==data['total_stored_records']
    expected={'cleaning':'9091','grounds':'773','it':'725','refurbishment':'45453'}
    assert {s['sector']:s['cpv_prefix'] for s in data['sectors']}==expected
    counts=[];countries=[];sources=[];deadlines=[]
    for sector in data['sectors']:
        code=sector['sector'];total=sector['active_future_deadline_records']
        assert type(total) is int and 0<=total<=data['active_future_deadline_records']
        assert len(sector['countries'])==len({r['country_code'] for r in sector['countries']})==43
        assert len(sector['sources'])==len({r['source_code'] for r in sector['sources']})
        assert len(sector['deadline_buckets'])==4
        assert sum(r['records'] for r in sector['sources'])==total
        assert sum(r['records'] for r in sector['deadline_buckets'])==total
        for row in sector['countries']:
            assert re.fullmatch('[A-Z]{3}',row['country_code']) and type(row['records']) is int and 0<=row['records']<=total
        assert 0<=sector['records_without_known_country']<=total
        for row in sector['sources']:
            assert row['source_url'].startswith('https://') and type(row['records']) is int and 0<row['records']<=total
        counts.append(dict(sector=code,name=sector['name'],cpv_prefix=sector['cpv_prefix'],records=total,records_without_known_country=sector['records_without_known_country']))
        countries.extend(dict(sector=code,**row) for row in sector['countries'])
        sources.extend(dict(sector=code,**row) for row in sector['sources'])
        deadlines.extend(dict(sector=code,**row) for row in sector['deadline_buckets'])
    assert max(s['active_future_deadline_records'] for s in data['sectors'])<=data['distinct_stored_records_in_selected_sectors']<=sum(s['active_future_deadline_records'] for s in data['sectors'])
    for filename,expected_rows in [('sectors.csv',counts),('countries.csv',countries),('sources.csv',sources),('deadlines.csv',deadlines)]:
        assert read_csv(path.parent/filename)==[{k:'' if v is None else str(v) for k,v in row.items()} for row in expected_rows],filename
    assert re.fullmatch('[a-f0-9]{64}',data['provenance']['exporter_sha256'])
    assert all(word not in data for word in ('email','profile','match_score','business_description','token','buyer','title'))
    print('PASS',path.parent.name,': four classifications, UTC capture, population/source/deadline partitions, country rows, CSV agreement and checksums')
