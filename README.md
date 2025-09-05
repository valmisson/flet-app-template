# Flet App Template

A small desktop application built with Flet. This repository is a lightweight
template and starting point for creating cross-platform desktop apps using
the Flet framework.

## Quick summary

- Project: A Flet-based desktop app template
- Python: requires 3.11+
- Key deps: `flet`, `pydantic`, `python-dotenv`, `loguru`, `sentry-sdk`

## Getting started

Prerequisites

- Python 3.11 or later
- Poetry (recommended) or pip

Install with Poetry (recommended):

```bash
poetry install
poetry run python main.py
```

Or using a virtual environment and pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r <(poetry export -f requirements.txt --without-hashes)
python main.py
```

Note: the project uses `pyproject.toml` / Poetry for dependency management. If
you prefer not to use Poetry, export a requirements file as shown above.

## Run

Start the app with:

```bash
python main.py
```

This launches the Flet application; the entry point is `main.py` which calls
the `AppWindow` class in `app/window.py`.

## Tests & development

Run the test suite with pytest:

```bash
poetry run pytest
```

Linters and type checks (installed in the dev group):

```bash
poetry run ruff check .
poetry run mypy .
```

Pre-commit hooks are configured in the project; run them locally with:

```bash
poetry run pre-commit run --all-files
```

## Project layout

- `main.py` — application entry point
- `app/` — package with UI code (`window.py`, views, components)
- `config/` — settings and logger configuration
- `tests/` — unit tests

## Notes

- The project metadata is in `pyproject.toml`. Update version/description there.
- If you plan to distribute the app, consider packaging options for Flet
	(desktop or web) and include platform-specific instructions.

## License

This project is licensed under the MIT License - see [LICENSE][license] for more information.

Copyright (c) 2025-present, Valmisson Grizorte.

[license]: https://github.com/valmisson/flet-app-template/blob/develop/LICENSE