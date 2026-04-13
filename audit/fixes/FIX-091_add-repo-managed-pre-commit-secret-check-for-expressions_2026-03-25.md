# FIX-091 — Add repo-managed pre-commit secret check for expressions

## Summary
- Added a PowerShell guard script to validate placeholder-safe values in staged `expressions.tmdl`.
- Added a repo-managed pre-commit hook under `.githooks/`.
- Added an installer script to configure `core.hooksPath` locally.
- Updated repository documentation to describe the automated guard.

## Why
- The repository still relied on a manual visual review before commit to avoid leaking `Param_TenantId`, `Param_ClientId`, or `Param_Secret`.
- This guard reduces the chance of committing live credentials by mistake.

## Scope
- `scripts/check-expressions-placeholders.ps1`
- `scripts/install-git-hooks.ps1`
- `.githooks/pre-commit`
- `README.md`
- `AGENTS.md`

## Validation
- Static validation only in source.
- Manual validation required:
  - Run `powershell -ExecutionPolicy Bypass -File scripts/install-git-hooks.ps1`
  - Stage a safe placeholder-only `expressions.tmdl` and confirm commit is allowed.
  - Stage a non-placeholder value and confirm commit is blocked.
