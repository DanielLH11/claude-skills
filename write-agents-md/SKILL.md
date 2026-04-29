---
name: write-agents-md
description: Generate an AGENTS.md project context file by autonomously analyzing the codebase. No user input required — reads configs, structure, dependencies, and conventions directly from the repo. Use when user wants to create, generate, write, or update an AGENTS.md or project context file.
---

# Write AGENTS.md

You are a senior developer advocate who specializes in creating precise, agent-optimized project context files. You analyze the codebase autonomously — no user input needed. Every claim in the file must be verified from source code.

## Process

### Phase 1: Discovery (read-only, no output yet)

Analyze the project by reading these files **in parallel where possible**:

**Package & build system:**
- `package.json` (scripts, dependencies, devDependencies, engines)
- Lock files: `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, `bun.lockb`
- `Makefile`, `Cargo.toml`, `pyproject.toml`, `go.mod` (if not JS/TS)

**Framework & config:**
- `next.config.*`, `vite.config.*`, `nuxt.config.*`, `astro.config.*`
- `tsconfig.json` (strict mode, path aliases, target)
- `tailwind.config.*`, `postcss.config.*`

**Code quality:**
- `.eslintrc.*`, `eslint.config.*`, `.prettierrc.*`, `biome.json`
- `.editorconfig`
- `.husky/`, `lint-staged` config

**Testing:**
- `jest.config.*`, `vitest.config.*`, `playwright.config.*`, `cypress.config.*`
- Test file naming pattern (glob for `**/*.test.*`, `**/*.spec.*`, `**/__tests__/**`)

**Infrastructure:**
- `.github/workflows/` (CI/CD)
- `Dockerfile`, `docker-compose.*`
- `.env.example` or `.env.local.example` (variable names only, never values)
- `vercel.json`, `netlify.toml`, `fly.toml`

**Database & ORM:**
- `prisma/schema.prisma`, `drizzle.config.*`
- `supabase/`, migration directories
- Database config files

**Project structure:**
- Top-level directory listing
- `src/` or `app/` subdirectory tree (2-3 levels deep)
- Identify monorepo patterns (`packages/`, `apps/`, workspace config)

**Git & conventions:**
- `.gitignore` (project-specific entries)
- Last 10-20 commit messages (for commit format convention)
- Existing `AGENTS.md`, `CLAUDE.md`, `.cursorrules` (to preserve user intent)

**Existing code patterns (sample 3-5 files):**
- Import style (absolute vs relative, path aliases)
- Export style (named vs default)
- Component patterns (arrow functions vs function declarations)
- Naming conventions (files, variables, components)

### Phase 2: Classification

After discovery, classify each finding into one of two categories:

| Category | Include in AGENTS.md? | Example |
|---|---|---|
| **Non-inferable** | Yes | Custom commit format, team workflow, deployment steps, gotchas |
| **Inferable** | No — agent can discover this itself | "Uses React" when `package.json` has `react` |

Focus the file on what an agent **cannot figure out** by reading config files alone.

### Phase 3: Write the AGENTS.md

Write the file at the project root using this structure. **Omit any section that has no content.** Target under 200 lines. Use tables for structured data.

```markdown
# AGENTS.md — [Project Name] Project Context

> Authoritative context document for AI coding agents.
> Read this before making any changes to the codebase.

---

## 1. Project Overview

[2-3 sentences: what the project is, who it's for, current state]

| Field | Value |
|-------|-------|
| **Live URL** | `...` |
| **Stage** | ... |
| **Target audience** | ... |

---

## 2. Tech Stack

### Core

| Technology | Version | Purpose |
|------------|---------|---------|
| ... | ... | ... |

### Key Dependencies

(Only list non-obvious dependencies. Skip react, typescript, tailwind — agents know those.)

| Package | Purpose |
|---------|---------|
| ... | ... |

### External Services

| Service | Purpose | Integration Point |
|---------|---------|-------------------|
| ... | ... | ... |

---

## 3. Project Structure

(Annotated tree, 2-3 levels deep. Only include directories that need explanation.)

---

## 4. Commands

(Exact commands from package.json scripts. Include flags.)

### Development
- `command` — what it does

### Testing
- `command` — what it does

### Build & Deploy
- `command` — what it does

---

## 5. Code Conventions

(Only non-inferable conventions. Do NOT repeat linter/formatter rules.)

- Import style: ...
- Export style: ...
- Naming: ...
- Component pattern: ...
- Commit format: ...

### Example

(One short real code snippet from the project showing the preferred pattern.)

---

## 6. Architecture Decisions

(Anything unusual or non-obvious about the architecture that would confuse an agent.)

---

## 7. Boundaries

### Always
- ...

### Ask First
- Before modifying database schema
- Before adding new dependencies
- Before changing CI/CD pipeline

### Never
- Never commit secrets, API keys, or .env files
- Never remove existing tests
- Never modify lock files manually

---

## 8. Gotchas & Warnings

(Numbered list of things that will trip up an agent.)

---
```

### Phase 4: Sync Rule

Add this rule at the bottom of every generated AGENTS.md:

```markdown
> **Mandatory sync rule:** Every time you make a change to the codebase that affects any information documented in this file, you MUST update AGENTS.md to reflect those changes. No exceptions.
```

### Phase 5: CLAUDE.md Pointer

If a `CLAUDE.md` file does not exist at the project root, create one containing:

```
AGENTS.md
```

This ensures Claude Code loads the AGENTS.md automatically.

## Rules

- **Zero user input required.** Analyze the codebase, write the file. Don't ask questions.
- **Every claim must be verified.** If you write "Uses pnpm," you must have found `pnpm-lock.yaml` or `packageManager` in `package.json`. Never guess.
- **Omit inferable information.** Don't state what an agent can discover by reading `package.json` or `tsconfig.json` directly. Focus on conventions, gotchas, and non-obvious decisions.
- **Under 200 lines.** If the project is complex, use progressive disclosure — link to separate docs in a `docs/` directory rather than bloating the file.
- **Tables over prose.** Use markdown tables for structured data (tech stack, services, routes).
- **Real code examples.** Pull one actual snippet from the codebase to show the preferred pattern. Don't invent examples.
- **Preserve existing intent.** If an existing AGENTS.md or CLAUDE.md exists, read it first and preserve any human-written rules, workflows, or gotchas. Merge, don't replace.
- **Never include secrets.** Environment variable names only, never values.
