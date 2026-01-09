# asteroids

## Here's how to use `uv` run

Run Python scripts:

```
uv run python main.py
uv run python -c "print('hello')"
```

Start a Python REPL:

```
uv run python
```

Install packages:

```
uv add <package-name> # Adds to pyproject.toml and installs
uv remove <package-name> # Removes from pyproject.toml
```

Run installed CLI tools:

```
uv run <tool-name>
```

Example:

```
uv run pytest
```

Run one-off commands with packages (without installing):

```
uv run --with <package> python -c "import <package>"
```

Example:

```
uv run --with requests python script.py
```
