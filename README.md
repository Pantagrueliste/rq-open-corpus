# RQ Open Corpus — the machine-readable Renaissance

The largest documented open aggregation of Renaissance primary sources (1450–1700):
**123,172 texts · 2,141,439,302 words · 79 languages · 273 collections** of transcribed
(keyed/corrected) text — the *clean corpus* behind the article *The Machine-Readable
Renaissance* and its coverage radiography against USTC.

**🗺️ Interactive explorer:** `web/index.html` (GitHub Pages once public).
**📦 Data:** the frozen metadata database + verification kit are attached to
[Releases](../../releases); the redistributable text archive lives on Hugging Face /
Zenodo (links added at article publication). 99.06% of words are SHA-256/commit-verified;
the kit lets anyone rebuild and byte-verify the corpus.

## Did we miss a corpus? → Contribute
This map is a first survey, drawn like the maps of the period it studies: openly
conjectural at the edges and meant to be corrected. Two ways, see **CONTRIBUTING.md**:
1. **Signal a corpus** (2 minutes): open an issue with the pointer.
2. **Submit texts** (PR): a staging JSONL, validated automatically.

## Versioning — read before citing
- **`v2026.06-frozen`** is the snapshot every number in the article is computed on. It never changes.
- Community submissions are ingested in a **release every 3–6 months** (`v2027.01`, …),
  each with a regenerated database, provenance manifest, and explorer.
- Cite the version you used. The article ≙ `v2026.06-frozen`, permanently.

## Governance
Submissions are reviewed against the criteria in CONTRIBUTING.md (in-window, open,
*transcription* not raw OCR, licensed, provenance stated). The maintainer runs the
ingest + dedup + manifest pipeline and freezes each release. Disagreements about
scope are argued in issues — in public, which is the point.
