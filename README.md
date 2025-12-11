# myproj

A simple Python project demonstrating modern packaging and testing practices.

## Installation

Install the project in editable mode. Development dependencies are available
as an extra declared in `pyproject.toml`:

```bash
pip install -e .[dev]
```

## Usage

Run the CLI

The package exposes a small CLI with two subcommands:

- `greet [NAME]` — print a greeting (defaults to "World")
- `cheatsheet` — generate a builtins cheatsheet and write it to a file

Examples (installed script):

```bash
# greet Alice
myproj greet Alice

# generate a markdown cheatsheet into docs/
myproj cheatsheet -o docs/builtins_cheatsheet.md -f markdown
```

Examples (module run):

```bash
# greet (module)
python -m myproj.cli greet Alice

# generate cheatsheet (module)
python -m myproj.cli cheatsheet -o builtins_cli.txt -f text
```

Or use the module directly:

```python
from myproj.core import greet

print(greet("Alice"))
```

## Development

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=myproj
```

## License

MIT
