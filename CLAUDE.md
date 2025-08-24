# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

This is a Python 3.10+ project using UV for package management. Key development commands:

- **Install dependencies**: `uv sync`
- **Run main application**: `uv run python main.py`
- **Run individual scripts**: `uv run python scripts/<script_name>.py`
- **Run Jupyter notebooks**: `uv run jupyter notebook`

## Project Structure

- **src/**: Core utility modules
  - `utils.py`: Text processing and file utilities
  - `helper.py`: Environment and API key management
  - `split_audio.py`: Audio processing utilities
  - `embedding_file.py`: File embedding functionality

- **scripts/**: Individual tool scripts for specific tasks
  - Audio processing: `audio2txt_tools.py`, `audio_process_tools.py`
  - Translation: Various translation scripts for different LLM providers
  - Text processing: `md_modify.py`, `replace_space.py`, `trim_extra_space.py`
  - YouTube integration: `youtube_download.py`

- **archived/**: Legacy scripts and tools
- **jupyter-notebook/**: Experimental notebooks for LLM workflows
- **prompt/**: Prompt templates for different LLM tasks
- **working/**: Temporary working files

## Key Dependencies

- LLM frameworks: `llama-index`, `langchain-openai`, `trulens-eval`
- LLM providers: Google Gemini, OpenAI, DeepSeek, Kimi, Zhipu, Bailian, etc.
- Audio processing: `insanely-fast-whisper`, `yt-dlp`
- Text processing: `pangu`, `pymupdf`, `pyperclip`
- Vector storage: `weaviate`

## Environment Configuration

Copy `.env.example` to `.env` and configure API keys for various LLM services:
- `GOOGLE_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`
- `KIMI_API_KEY`, `ZHIPU_API_KEY`, `BAILIAN_API_KEY`
- `MISTRAL_API_KEY`, `FIREWORKS_API_KEY`, `SILICON_API_KEY`
- `WCD_API_KEY` for Weaviate vector database

## Common Development Tasks

1. **Adding new LLM provider**: Update `src/helper.py` with new API key mapping
2. **Creating new translation script**: Follow patterns in `scripts/` directory
3. **Text processing utilities**: Add to `src/utils.py`
4. **Audio processing**: Use `src/split_audio.py` and related scripts

## Architecture Notes

- The project uses a modular approach with shared utilities in `src/`
- Individual scripts are self-contained for specific tasks
- Environment configuration is centralized in `src/helper.py`
- Prompt templates are stored separately in `prompt/` directory
- Jupyter notebooks are used for experimentation and prototyping