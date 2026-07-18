# Contributing a corpus

## Path 1 — Signal (an issue, 2 minutes)
You know an open corpus of transcribed 1450–1700 text we missed? Open a
**Corpus suggestion** issue. Name, URL, license, language(s), rough size. That's it —
signalements are triaged every release cycle and credited in the release notes.

## Path 2 — Submit (a pull request with the texts)
Add a file `submissions/<YourCollectionName>/<YourCollectionName>.jsonl`, one JSON
object per text:

```json
{"collection": "MyCorpus", "filename": "unique_name.txt", "raw": "the full text…",
 "language": "ita", "year": 1547, "source": "Project X (https://…)",
 "license": "CC-BY 4.0", "quality_rating": 4}
```

| Field | Required | Notes |
|---|---|---|
| `collection` | yes | one collection per PR, stable name |
| `filename` | yes | unique within the collection |
| `raw` | yes | plain text (UTF-8). TEI/XML also accepted — say so in the PR |
| `language` | yes | ISO 639-3 |
| `year` | yes | composition/printing year; `null` only if genuinely unknown |
| `source` | yes | where the transcription comes from (project + URL) |
| `license` | yes | the UPSTREAM license (CC-*, PD, or "see source") |
| `quality_rating` | no | 1–5 (5 = proofread keyed text; see below) |

### Inclusion criteria (what the validator + review check)
1. **In window**: produced 1450–1700 (scope = the European Renaissance *and its
   encounters* — mission imprints in any language qualify; autochthonous non-European
   heartland literatures do not).
2. **Transcription, not raw OCR**: keyed or corrected text. Uncorrected OCR dumps
   belong to the *dirty corpus* tier and are tracked separately — flag them honestly
   and they may be listed, not ingested.
3. **Open**: publicly reachable without subscription; state the license. No pirated
   or ToS-violating material, ever.
4. **Provenance**: the transcribing project must be named. You may submit your own
   editions — that is rather the idea.

CI validates schema/language codes/window/duplicates automatically on the PR.
A human (the maintainer) reviews scope and license before merge. Merged submissions
enter the next release's ingest run (dedup + manifest + quality tiering) and are
credited in the release notes and the corpus's ATTRIBUTIONS table.
