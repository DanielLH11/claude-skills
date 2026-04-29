# README Reference Templates

---

## Badges

Use [shields.io](https://shields.io). Pick **2–4 badges max** at the top. Add more in a dedicated section further down.

```md
<!-- Build / CI -->
![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)

<!-- npm version -->
[![npm version](https://img.shields.io/npm/v/PACKAGE.svg?style=flat)](https://www.npmjs.com/package/PACKAGE)

<!-- PyPI version -->
[![PyPI version](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- Coverage -->
[![Coverage](https://img.shields.io/codecov/c/github/USER/REPO.svg)](https://codecov.io/gh/USER/REPO)

<!-- Downloads -->
[![npm downloads](https://img.shields.io/npm/dm/PACKAGE.svg)](https://www.npmjs.com/package/PACKAGE)
```

Style options: `?style=flat` (default), `?style=flat-square`, `?style=for-the-badge`

---

## Library / Package

```md
# package-name

[![npm version](https://img.shields.io/npm/v/package-name.svg?style=flat)](https://www.npmjs.com/package/package-name)
[![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USER/REPO/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> One-sentence description of what this library does and why it exists.

## Features

- Feature one — brief explanation
- Feature two — brief explanation
- Feature three — brief explanation

## Installation

```bash
npm install package-name
# or
yarn add package-name
```

## Usage

```js
import { thing } from 'package-name';

const result = thing({ option: 'value' });
console.log(result);
```

## API

### `thing(options)`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `option` | `string` | `'default'` | What it controls |

**Returns:** `string` — description of the return value.

## Requirements

- Node.js ≥ 18
- (any other peer deps)

## Contributing

Pull requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE) © Your Name
```

---

## CLI Tool

```md
# tool-name

[![npm version](https://img.shields.io/npm/v/tool-name.svg?style=flat)](https://www.npmjs.com/package/tool-name)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> One-line pitch: what problem this CLI solves and for whom.

## Installation

```bash
npm install -g tool-name
# or run without installing
npx tool-name
```

## Usage

```bash
tool-name [options] <input>
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-o, --output <path>` | Output file path | `./output` |
| `-v, --verbose` | Enable verbose logging | `false` |
| `--version` | Print version | — |

### Examples

```bash
# Basic usage
tool-name input.txt

# With options
tool-name --output dist/ --verbose input.txt
```

## Requirements

- Node.js ≥ 18

## License

[MIT](LICENSE) © Your Name
```

---

## Web App

```md
# App Name

[![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USER/REPO/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> One-sentence description of the app and who it's for.

![Screenshot](docs/screenshot.png)

## Features

- Feature 1
- Feature 2
- Feature 3

## Tech Stack

- **Framework:** Next.js 15 / React 19
- **Styling:** Tailwind CSS
- **Database:** PostgreSQL + Prisma
- **Auth:** (your auth solution)
- **Deployment:** Vercel / Railway

## Getting Started

### Prerequisites

- Node.js ≥ 18
- PostgreSQL (or Docker)

### Installation

```bash
git clone https://github.com/USER/REPO.git
cd REPO
npm install
cp .env.example .env   # fill in values
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://...` |
| `SECRET_KEY` | Auth secret | random 32-char string |

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start dev server |
| `npm run build` | Production build |
| `npm test` | Run tests |

## Deployment

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

## Contributing

1. Fork the repo
2. Create your branch: `git checkout -b feat/my-feature`
3. Commit: `git commit -m 'feat: add my feature'`
4. Push and open a PR

## License

[MIT](LICENSE) © Your Name
```

---

## API / Backend

```md
# api-name

[![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USER/REPO/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> REST/GraphQL API for [what it serves]. Built with [framework].

## Base URL

```
https://api.example.com/v1
```

## Authentication

Include `Authorization: Bearer <token>` in all requests.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/users` | List users |
| `POST` | `/users` | Create user |
| `GET` | `/users/:id` | Get user by ID |

## Quick Example

```bash
curl -H "Authorization: Bearer TOKEN" \
  https://api.example.com/v1/users
```

## Local Development

```bash
git clone https://github.com/USER/REPO.git
cd REPO
cp .env.example .env
docker compose up -d   # starts DB
npm install
npm run dev
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `JWT_SECRET` | Yes | Token signing secret |
| `PORT` | No | Server port (default: 3000) |

## Running Tests

```bash
npm test          # unit tests
npm run test:e2e  # integration tests
```

## License

[MIT](LICENSE) © Your Name
```

---

## OSS Generic

```md
# Project Name

[![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USER/REPO/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> One-line description. What it is, what problem it solves.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

2–3 paragraphs: background, motivation, who it's for.

## Getting Started

### Prerequisites

- Requirement 1 (version X or higher)
- Requirement 2

### Installation

```bash
# clone
git clone https://github.com/USER/REPO.git
cd REPO

# install
[install command]

# configure
cp .env.example .env
```

## Usage

[Minimal working example with code block and output]

## Roadmap

- [x] Initial release
- [ ] Planned feature 1
- [ ] Planned feature 2

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

1. Fork the project
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
```

---

## Checklist Before Saving

- [ ] Title is specific (not "My Project")
- [ ] One-line description answers: what + why + who
- [ ] All code blocks have language identifiers
- [ ] Install commands are copy-paste-ready and accurate
- [ ] No placeholder text remains (`[TODO]`, `your description here`)
- [ ] License section is present
- [ ] For UI projects: at least one screenshot or demo link
- [ ] Badges use consistent style
