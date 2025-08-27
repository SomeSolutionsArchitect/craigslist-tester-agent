# Craigslist-tester-agent

Lightweight automation utilities and example agents for driving a browser-based QA workflow (used with the `browser-use` automation agent).

This repository contains small scripts and a sample feature describing a Craigslist QA task (navigate to Miami Craigslist, find the 'boats' listing, and verify filtering behavior). It's intended as a compact playground for browser-driven acceptance testing and experiment with the `browser-use` agent.

## Quick overview

- Project: `craigslist-tester-agent`
- Purpose: automation scripts and artifacts that demonstrate driving a browser to execute acceptance-style scenarios against websites (example: Craigslist boats-for-sale).
- Primary files:
  - `boats-for-sale.feature.md` — feature scenarios to validate on miami.craigslist.org
  - `agent.py` — example runner/agents (small scripts)

## Requirements

* Python 3.13+ (project `pyproject.toml` indicates >=3.13)
* [uv package manager](https://github.com/astral-sh/uv) (required for environment setup and running scripts)

## Environment variables

You may need to provide API keys or other configuration via environment variables. The recommended approach is to create a `.env` file in the project root and set any required variables there. For example:

```bash
# .env
BROWSER_USE_API_KEY=your_api_key_here
```

Alternatively, you can set environment variables directly in your shell before running the agent scripts. Make sure any required secrets or configuration are available to the agent at runtime.

## Getting started

1. Clone the repo and open it in VS Code.
2. Use [uv](https://github.com/astral-sh/uv) to set up your Python environment and sync dependencies:

```bash
uv venv
source .venv/bin/activate
uv sync
```

3. Review the `boats-for-sale.feature.md` to understand the acceptance scenarios to run. The repository contains small example scripts (`main.py`, `agent.py`) that show how an automation agent could be used to run the scenarios.

## Running the example 

This repository is a demonstration; there is no single turnkey CLI included. Typical steps to exercise the examples:

1. Start the `browser-use` automation server (per your local setup).
2. Run the agent script to start the scripted agent logic that navigates to craigslist and runs the scenarios. For example:

```bash
uv run agent.py
```

Expect the agent to open a browser session, navigate to `https://miami.craigslist.org`, and perform the checks described in `boats-for-sale.feature.md`. The exact output depends on your automation backend configuration.

## Files of interest

- `boats-for-sale.feature.md` — feature file describing the QA scenarios.
- `README.md` — this file.

## How to contribute

This repo is a personal/sandbox project. Small improvements are welcome: add tests, improve the feature file, or wire a more robust runner. When in doubt, open an issue listing what you'd like to change.

---