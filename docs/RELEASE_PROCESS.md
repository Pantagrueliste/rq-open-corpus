# Release process (maintainer, every 3–6 months)
1. Triage open corpus-suggestion issues; thank + close-or-queue each.
2. For merged submissions in `submissions/`: run the ingest pipeline
   (`ingest_from_staging.py` + `manifest_add.py` from the kit) on a working copy —
   NEVER on the frozen snapshot.
3. Run dedup views + `rebuild_source_audit.py` (must report missing: 0) +
   `rebuild_raw_tree_lock.py` for new sources.
4. Regenerate: canonical numbers, inverse index CSVs, explorer data JSON → `web/`.
5. Tag `vYYYY.MM`; attach the new metadata DB + updated kit to the GitHub Release;
   mirror to HF/Zenodo (new version, new DOI); write release notes with the diff
   and contributor credits.
6. Update the README headline numbers WITH the version tag next to them.
