# Repository Guidelines

This repository houses a suite of Python 3.10+ utilities for LLM-driven media processing, prompt workflows, and integration helpers. Follow the guidance below to keep contributions cohesive and production-ready.

## Project Structure & Module Organization
- `src/`: Core helpers (API key loading, text formatting, audio splitting) reused by scripts.
- `scripts/`: Task-specific CLIs (audio transcription, Gemini translation, YouTube downloads); each script expects dependencies defined in `pyproject.toml`.
- `prompt/`, `information_anlaysis/`, `mermaid/`: Supporting assets for prompt engineering, knowledge analyses, and diagrams.
- `working/`: Scratch space for in-progress inputs/outputs; clean up temporary files before committing.
- `archived/` and `jupyter-notebook/`: Historical references and exploratory notebooks—do not depend on them for runtime code.

## Build, Test, and Development Commands
```bash
python -m venv .venv && source .venv/bin/activate  # local virtualenv
pip install -r requirements.txt                    # install runtime deps (use `uv sync` if you prefer uv)
python main.py                                     # smoke-test the environment
python scripts/chat_with_llm.py --mode zh          # example: run chat pipeline using working/input.md
```
Run scripts from the repo root so relative imports resolve without extra `PYTHONPATH` tweaks.

## Coding Style & Naming Conventions
- Use 4-space indents, `snake_case` modules/functions, and descriptive docstrings (bilingual where helpful, matching existing tone).
- Keep shared logic inside `src/`; scripts should remain thin orchestration layers with `argparse` entry points.
- Add type hints for new public functions and validate I/O paths with `pathlib.Path`.
- Never hardcode secrets—load via `src.helper.get_api_key()`/`get_base_url()`.

## Testing Guidelines
- Prefer lightweight `pytest` cases alongside new modules under a `tests/` directory; name files `test_<feature>.py`.
- For CLI tools, pair unit coverage with sample fixtures stored in `working/` or an `examples/` subfolder and document manual steps in the PR.
- Share captured outputs when adding streaming interactions so reviewers can confirm behavior without rerunning.

## Commit & Pull Request Guidelines
- Follow existing short, imperative summaries (e.g., `Add Skilljar downloader`, `20250918-mac` for dated drops). Reference issue IDs when available.
- Ensure commits are focused; large features should be split across logical commits.
- PRs must describe the change, list verification steps (commands/tests run), and note any required API keys or config files.
- Include before/after context or screenshots when modifying user-facing artifacts or generated documents.

## Security & Configuration Tips
- Store credentials in a local `.env`; never commit secrets. Document any new env keys in the PR.
- Review dependencies added to `pyproject.toml` for license compatibility and pin exact versions when introducing new integrations.
