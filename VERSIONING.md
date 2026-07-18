# Versioning policy
- `v2026.06-frozen` — the article snapshot (2026-06-26). Immutable. All published
  figures/claims trace to it.
- `vYYYY.MM` — semiannual (3–6 months) community releases: merged submissions ingested,
  deduplicated, manifest-registered; database + explorer regenerated; diffs summarized
  in release notes (words/languages/collections added, index cells that moved).
- Between releases, `main` may hold merged-but-not-ingested submissions in `submissions/`.
- Nothing is ever silently recomputed: every release states its snapshot date and the
  article's numbers remain those of `v2026.06-frozen`.
