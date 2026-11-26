"""Verify the aggregate-only trade summary, without network access."""
from pathlib import Path
from datetime import datetime,timedelta
import csv,hashlib,json,re

def verify_recent(root):
 paths=list((root/'trade-summaries').glob('*/summary.json'))
 assert paths,'No recent summaries'
 for path in paths:
  data=json.loads(path.read_text(encoding='utf-8'))
  assert set(data)=={'schema_version','as_of_utc','definition','provenance','sectors'}
  assert data['schema_version']=='trade-summary-1.0'
  instant=datetime.fromisoformat(data['as_of_utc'])
  assert instant.utcoffset()==timedelta(0) and path.parent.name==instant.strftime('%Y%m%dT%H%M%SZ')
  assert re.fullmatch('[a-f0-9]{64}',data['provenance']['source_json_sha256'])
  assert data['provenance']['source_json'].startswith('https://getcontractalerts.com/static/data/')
  expected={'cleaning':'9091','grounds':'773','it':'725','refurbishment':'45453'}
  assert {s['key']:s['cpv_prefix'] for s in data['sectors']}==expected
  expected_csv=[]
  for sector in data['sectors']:
   assert set(sector)=={'path','key','name','cpv_prefix','records','deadline_buckets','countries'}
   assert type(sector['records']) is int and sector['records']>=0
   assert sector['path'] in {'/tenders/cleaning','/tenders/grounds-maintenance','/tenders/it-support','/tenders/refurbishment'}
   assert [b['label'] for b in sector['deadline_buckets']]==['Within 3 days','3 to 7 days','7 to 14 days','More than 14 days']
   assert all(set(b)=={'label','records'} and type(b['records']) is int and b['records']>=0 for b in sector['deadline_buckets'])
   assert sum(b['records'] for b in sector['deadline_buckets'])==sector['records']
   assert len(sector['countries'])==len({c['code'] for c in sector['countries']})
   for country in sector['countries']:
    assert set(country)=={'code','country','records'}
    assert re.fullmatch('[A-Z]{3}',country['code']) and type(country['records']) is int and 0<=country['records']<=sector['records']
   expected_csv.append({'name':sector['name'],'cpv_prefix':sector['cpv_prefix'],'records':str(sector['records']),**{b['label']:str(b['records']) for b in sector['deadline_buckets']}})
  with (path.parent/'sectors.csv').open(encoding='utf-8',newline='') as stream:assert list(csv.DictReader(stream))==expected_csv
  print('PASS',path.parent.name,': aggregate field allowlist, UTC capture, deadline partitions, country formats and CSV agreement')

if __name__=='__main__':verify_recent(Path(__file__).resolve().parent)
