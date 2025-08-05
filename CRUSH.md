# CRUSH.md - Python Project Commands & Style Guide

## Build/Test/Lint Commands
```bash
# Install dependencies with uv
uv sync --upgrade --extra dev

# Run all tests. Check CI file for full list of commands.
uv run pytest

# Lint & format
uv run pre-commit run --all
```

## Code Style Guidelines
- **Imports**: Absolute imports only, sorted by ruff (stdlib → third-party → first-party)
- **Formatting**: 100 char line limit, single quotes, double quotes for docstrings
- **Types**: Use type hints, prefer specific types over Any, runtime-evaluated for Pydantic
- **Naming**: snake_case for functions/vars, PascalCase for classes, UPPER_SNAKE for constants
- **Error handling**: Use specific exception types, avoid bare except, log appropriately
- **Docstrings**: Use double quotes, Google style format
- **Complexity**: Max 17 McCabe, max 15 args, max 5 positional args
- **Line length**: 100 characters max
