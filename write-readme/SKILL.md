---
name: write-readme
description: Write a professional README.md for any project type (library, CLI, web app, API, OSS). Researches the codebase, identifies the project type, and generates a polished README with the right sections, badges, and examples. Use when user wants to create, write, generate, or improve a README file, mentions "README", "documentation", or "project docs".
---

# Write README

## Quick Start

1. Explore the project: read `package.json`, `pyproject.toml`, `Cargo.toml`, or equivalent — detect language, dependencies, entry points, scripts
2. Identify the project type (see **Project Types** below)
3. Pick the matching template from [REFERENCE.md](REFERENCE.md)
4. Fill every section — never leave placeholders like `[TODO]`
5. Write the file as `README.md` in the project root

---

## Project Types

| Type | Key signals | Template |
|------|-------------|----------|
| **Library / Package** | `exports`, `main`, published to npm/PyPI | [Library](REFERENCE.md#library--package) |
| **CLI Tool** | `bin` field, `argv`, `commander`, `click` | [CLI](REFERENCE.md#cli-tool) |
| **Web App** | `next`, `vite`, `react`, `vue`, routes, pages | [Web App](REFERENCE.md#web-app) |
| **API / Backend** | `express`, `fastapi`, `django`, REST/GraphQL routes | [API](REFERENCE.md#api--backend) |
| **OSS / Generic** | Anything else | [OSS Generic](REFERENCE.md#oss-generic) |

---

## Required Sections (all types)

- [ ] **Title + one-line description** — clear, specific, no filler words
- [ ] **Badges** — 2–4 max at top (build, version, license). See [badges guide](REFERENCE.md#badges)
- [ ] **What it does** — 2–3 sentences: *what*, *why*, *who for*
- [ ] **Features** — bullet list of 4–8 key capabilities
- [ ] **Prerequisites / Requirements** — OS, runtime version, env vars
- [ ] **Installation** — copy-paste-ready commands (no "you may need to")
- [ ] **Usage** — at least one complete working example with code block
- [ ] **License** — SPDX identifier + link

## Optional (add when relevant)

- [ ] **Table of Contents** — only if README exceeds ~150 lines
- [ ] **Screenshots / Demo GIF** — always include for UI projects
- [ ] **Configuration** — env vars table, config file options
- [ ] **API Reference** — for libraries / backends
- [ ] **Roadmap** — for OSS projects
- [ ] **Contributing** — link to CONTRIBUTING.md or inline guide
- [ ] **Acknowledgements** — credits, inspirations

---

## Quality Rules

- **No placeholders** — every section must be complete, not `[your description here]`
- **Test your install steps** — commands must be accurate for the detected stack
- **Code blocks always specify language** — ` ```bash ` not ` ``` `
- **Active voice** — "Installs dependencies" not "Dependencies are installed"
- **Badges from shields.io** — consistent style; use `flat` or `for-the-badge`
- **One screenshot minimum** for any project with a UI

See [REFERENCE.md](REFERENCE.md) for full templates and badge snippets.
