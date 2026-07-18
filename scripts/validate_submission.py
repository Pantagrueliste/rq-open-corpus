#!/usr/bin/env python3
"""Validate corpus submissions (staging JSONL). Stdlib only; used by CI and locally:
   python scripts/validate_submission.py submissions/MyCorpus/MyCorpus.jsonl"""
import json, re, sys

REQ = ["collection", "filename", "raw", "language", "year", "source", "license"]
ISO3 = re.compile(r"^[a-z]{3}$")

def validate(path):
    errs, warns, n, inwin, words = [], [], 0, 0, 0
    seen = set()
    colls = set()
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip(): continue
        try:
            r = json.loads(line)
        except Exception as e:
            errs.append(f"L{i}: invalid JSON ({e})"); continue
        n += 1
        for k in REQ:
            if k == "year": continue
            if not r.get(k): errs.append(f"L{i}: missing/empty '{k}'")
        if "year" not in r: errs.append(f"L{i}: missing 'year' (use null only if unknown)")
        lang = r.get("language") or ""
        if lang and not ISO3.match(lang): errs.append(f"L{i}: language '{lang}' is not ISO 639-3 (3 lowercase letters)")
        y = r.get("year")
        if isinstance(y, int):
            if 1450 <= y <= 1700: inwin += 1
            elif y < 1200 or y > 2030: errs.append(f"L{i}: implausible year {y}")
        fn = r.get("filename")
        if fn in seen: errs.append(f"L{i}: duplicate filename '{fn}'")
        seen.add(fn); colls.add(r.get("collection"))
        w = len((r.get("raw") or "").split()); words += w
        if 0 < w < 20: warns.append(f"L{i}: very short text ({w} words)")
    if len(colls) > 1: errs.append(f"multiple collections in one file: {colls} (one collection per PR)")
    if n and inwin / n < 0.5: warns.append(f"only {inwin}/{n} texts dated in-window 1450–1700 — scope review needed")
    print(f"{path}: {n} texts · {words:,} words · {inwin} in-window · {len(errs)} errors · {len(warns)} warnings")
    for e in errs[:25]: print("  ERROR:", e)
    for w_ in warns[:10]: print("  warn :", w_)
    return not errs

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files: print("no submission files changed"); sys.exit(0)
    ok = all(validate(f) for f in files)
    sys.exit(0 if ok else 1)
