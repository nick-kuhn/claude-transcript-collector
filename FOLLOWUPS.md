# Follow-ups

(GitHub Issues are disabled on this repo, so tracked here.)

## Open

_None currently._

## Done

- **Resilient + parallel uploads**: size-budgeted resumable units, background-job
  execution with a progress bar, and concurrent unit uploads
  (`CTC_UPLOAD_CONCURRENCY`).
- **Pi (`pi-subagents`) task subagents** collected + marked: run-dir transcripts
  `<parent>/<runId>/run-N/session.jsonl` (parent from the path) and forked
  sessions (parent from the `parentSession` header). `events.jsonl` and
  `subagent-artifacts/*.jsonl` are excluded (only `session.jsonl` is matched).
- **Credential redaction decoupled from the PII toggle**: Neon/RunPod/DB-URI
  patterns added to the secret pass; secret/credential redaction is always-on.
- **Codex subagent classification** aligned to the real `SessionSource` schema
  (drop review/compact/memory_consolidation/internal; keep+mark thread_spawn
  with `parent_thread_id`, and the `other` catch-all).

## Dropped

- **Durable secret-scanner** (detect-secrets / structural URI / entropy) — too
  slow. The high-precision per-provider regex patterns are the retained approach.
  Known accepted limitations: GitHub-handle redaction (needs an account lookup,
  not a pure regex) and third-party names in free text are not redacted.
