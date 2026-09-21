# demo — a governance demo fixture

**This repository is a test fixture, not a real service.** It exists to demonstrate a governed
AI-workforce platform acting on a repository: an agent takes an issue to a *draft* pull request,
and is refused when it tries to merge its own work.

Nothing here is deployed, connects to anything, or handles real data. `src/lookup.py` contains a
**deliberate SQL-injection pattern** so that CodeQL raises an alert for the remediation demo. Do
not copy it.

| File | Purpose |
|---|---|
| `src/lookup.py` | deliberate SQLi pattern — the code-scanning alert fixture |
| `src/report.py` | small, well-specified bug — the issue-to-pull-request fixture |
