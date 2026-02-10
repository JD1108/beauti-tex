# beauti-tex v0.1.0a3.dev0+g83e19fe70.d20260209

A Python library for generating clean and configurable LaTeX documents from templates.

## Installation

```bash
pip install beauti-tex
```

## Quick Start

```python
from beauti_tex import projBuilder

projBuilder("Project Name")
```

## API Documentation

_This section is automatically generated from docstrings._

#### `projBuilder()`

Creates a basic LaTeX Project for academic papers

Args:

    projName (str): Name of the project / main folder.

    projPath (Path | None): Optional base directory. Default is the current working directory.

    cfgPath (Path | None): Optional path to a configuration INI file.

Raises:

    FileExistsError: If the project folder already exists.

    FileNotFoundError: If template files are not found

Example:

    >>> projBuilder("MyPaper")

## License

Apache-2.0
