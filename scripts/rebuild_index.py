#!/usr/bin/env python3
"""Regenerate NOTE_INDEX.json exactly from manifest.json and notes/*.md."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RX=re.compile(r"^-?\s*\*\*(What it is|Key concepts|How you'd use it|LLM angle|Pitfalls & lessons|Verdict)\*\*\s*[—:-]?\s*(.*)$",re.M)
def fields(path):
 t=path.read_text(encoding='utf-8');ms=list(RX.finditer(t));out={}
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else t.find('\n## Sources consulted',m.end())
  if end<0:end=len(t)
  out[m.group(1)]=(m.group(2)+'\n'+t[m.end():end]).strip()
 return out
manifest=json.loads((ROOT/'manifest.json').read_text())
rows=[]
for entry in manifest:
 if entry['status']!='noted':continue
 slug=entry['slug'];path=ROOT/'notes'/f'{slug}.md';parsed=fields(path)
 if len(parsed)!=6:raise SystemExit(f'{slug}: expected six fields, found {sorted(parsed)}')
 rows.append({'slug':slug,'name':entry['name'],'section':entry['section'],'kind':entry['kind'],'note':f'notes/{slug}.md','fields':parsed})
(ROOT/'NOTE_INDEX.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print(f'Wrote {len(rows)} records to NOTE_INDEX.json')
