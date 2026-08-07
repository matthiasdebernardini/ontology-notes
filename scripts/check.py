#!/usr/bin/env python3
"""Validate the distributable ontology knowledge base and skill artifacts."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LABELS=["What it is","Key concepts","How you'd use it","LLM angle","Pitfalls & lessons","Verdict"]
RX=re.compile(r"^-?\s*\*\*(What it is|Key concepts|How you'd use it|LLM angle|Pitfalls & lessons|Verdict)\*\*\s*[—:-]?\s*(.*)$",re.M)
errors=[]
def fields(path):
 t=path.read_text(encoding="utf-8");ms=list(RX.finditer(t));out={}
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else t.find("\n## Sources consulted",m.end())
  if end<0:end=len(t)
  out[m.group(1)]=(m.group(2)+"\n"+t[m.end():end]).strip()
 return out
def need(ok,msg):
 if not ok:errors.append(msg)
manifest=json.loads((ROOT/'manifest.json').read_text())
index=json.loads((ROOT/'NOTE_INDEX.json').read_text())
need(len({r.get('slug') for r in manifest})==len(manifest),'duplicate manifest slug')
need(all(r.get('status') in {'noted','skipped'} for r in manifest),'nonterminal manifest status')
need(all(str(r.get('skip_reason','')).strip() for r in manifest if r.get('status')=='skipped'),'unreasoned skip')
noted={r['slug']:r for r in manifest if r['status']=='noted'}
note_slugs={p.stem for p in (ROOT/'notes').glob('*.md')}
need(note_slugs==set(noted),f"note mismatch: extra={sorted(note_slugs-set(noted))}, missing={sorted(set(noted)-note_slugs)}")
idx={r.get('slug'):r for r in index}
need(len(idx)==len(index),'duplicate NOTE_INDEX slug')
need(set(idx)==set(noted),'NOTE_INDEX slugs do not mirror noted manifest entries')
for slug,entry in noted.items():
 p=ROOT/'notes'/f'{slug}.md'
 if not p.is_file():continue
 f=fields(p);need(set(f)==set(LABELS),f'{slug}: six-field template mismatch')
 need(all(f.get(k,'').strip() for k in LABELS),f'{slug}: empty note field')
 if slug in idx:
  need(idx[slug].get('fields')==f,f'{slug}: NOTE_INDEX text is stale')
  need(idx[slug].get('note')==f'notes/{slug}.md',f'{slug}: wrong indexed note path')
syn=(ROOT/'SYNTHESIS.md').read_text();citations=re.findall(r'\[[^\]]*\]\((notes/[^)]+\.md)\)',syn)
need(len(set(citations))>=15,'SYNTHESIS cites fewer than 15 distinct notes')
for c in set(citations):need((ROOT/c).is_file(),f'broken synthesis citation: {c}')
need((ROOT/'skills/ontology-chat/SKILL.md').is_file(),'ontology-chat SKILL.md missing')
need((ROOT/'skills/ontology-chat/scripts/ontology_kb.py').is_file(),'ontology-chat retrieval CLI missing')
if errors:
 print(f'FAIL: {len(errors)} error(s)',file=sys.stderr)
 for e in errors:print(f'- {e}',file=sys.stderr)
 raise SystemExit(1)
print(f"PASS: {len(manifest)} manifest entries, {len(noted)} notes, {len(index)} index rows, and {len(set(citations))} synthesis citations validated.")
