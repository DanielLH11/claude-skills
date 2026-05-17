---
name: flow
description: Run the full feature pipeline from a curated prompt — generate a PRD, break it into tracker issues, then push the current branch. Use when the user invokes /flow, asks to "ship a feature end-to-end", or wants to chain PRD → issues → branch push in one step.
---

# Flow

Pipeline: **curated prompt → /to-prd → /to-issues → push branch**.

The user's `$ARGUMENTS` is the curated feature prompt.

## Preflight (abort on failure)

1. Run `git rev-parse --abbrev-ref HEAD`.
2. If branch is `master` or `main`: **STOP**. Tell the user to create a feature branch (suggest `git checkout -b feat/<slug>`) and re-run.
3. Run `git status --porcelain`. If there are uncommitted changes, ask the user whether to commit, stash, or abort before continuing.

## Steps

1. **PRD** — invoke the `to-prd` skill with the curated prompt as context. Let it publish to the issue tracker (full pipeline). Capture the resulting PRD reference (issue URL / ID).
2. **Issues** — invoke the `to-issues` skill against that PRD. Let it create the sub-issues on the tracker.
3. **Commit any new local files** produced by steps 1–2 (e.g. PRD markdown, plan files). Commit message: short summary referencing the PRD. **Do not include the `Co-Authored-By: Claude` trailer or any Anthropic attribution.** Use a plain HEREDOC body.
4. **Push the branch** with `git push -u origin <current-branch>`. Never push to `master`/`main`. Never use `--force` / `--force-with-lease` unless the user explicitly asks.
5. Report: branch name, PRD link, issue links, push result.

## Commit rules

- No `Co-Authored-By:` lines.
- No "🤖 Generated with Claude Code" footer.
- Honor pre-commit hooks; if a hook fails, fix and create a **new** commit (do not `--amend`, do not `--no-verify`).

## Guardrails

- If at any step the current branch becomes `master`/`main`, abort immediately.
- If `to-prd` or `to-issues` fails, stop and surface the error — do not push a partial state.
- Do not open a PR unless the user asks.
