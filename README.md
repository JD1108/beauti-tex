# beauti-tex v0.1.0


A Python library for generating clean and configurable LaTeX documents from templates.


## Installation


```bash

pip install beauti-tex

```


## Quick Start


### Paket


```python

from beauti_tex.proj_builder import make_project

make_project("Project Name")

```


### Command line


```bash

beauti-tex make-project -N MyPaper

```


## API Documentation


_This section is automatically generated from docstrings._


### `beauti_tex`


Beauti-tex package initializer.

This module exposes the main public API for beauti-tex, including
project creation and configuration management.

Public API:
  - make_project: Create a structured LaTeX project.
  - Config: Dataclass representing project configuration.
  - get_config: Load configuration from INI files.

Version:
  0.1.0


### `beauti_tex.cli`


Command-line interface for the beauti-tex package.

This module defines the CLI using argparse and connects user commands
to the internal project-building functionality.


#### `main()`


Entry point for the beauti-tex command-line interface.

This function sets up argument parsing, registers available
subcommands, and dispatches execution to the selected handler.


#### `make_cli()`


Handle the `make-project` CLI command.

This function serves as a thin adapter between the argparse
namespace and the internal `make_project` function.
**Args:**
- `args` (`argparse.Namespace`): Parsed command-line arguments with
  the following attributes:
  - name (str): Name of the LaTeX project.
  - project_path (str | None): Target directory for the project.
  - config_path (str | None): Path to a configuration file.


### `beauti_tex.config`


Configuration handling for beauti-tex.

This module provides utilities to load project configuration from INI files
and convert it into a structured `Config` dataclass. It reads default values
from `default.ini` and optionally merges user-provided configuration.

Included classes:
- Config
  Dataclass representing the configuration for a LaTeX project.

Included functions:
- get_config(path:Path | str |None=None)->Config
  Load and parse the configuration for a LaTeX project.


#### `get_config()`


Load and parse the configuration for a LaTeX project.

Reads default settings from `default.ini` located in the same directory
as this module. If an optional user configuration file is provided,
its settings override the defaults.
**Args:**
- `path` (`Path | str | None`): Optional path to a user-provided configuration INI file.
**Returns:**
  Config: A populated Config dataclass instance with all project settings.
**Raises:**
  FileNotFoundError: If the default INI file or the user-provided file does not exist,
  or if the template directory does not exist.


#### Class `Config`


Dataclass representing the configuration for a LaTeX project.

Attributes:
- `folders` (`list[str]`): List of folder names to create in the project.
- `chapters` (`list[str]`): List of chapter filenames to generate.
- `style` (`str`): Document style or template identifier.
- `temp_path` (`Path`): Path to template files for project generation.
- `size` (`int`): Paper size (e.g., 10, 11, 12 pt).
- `clas` (`str`): LaTeX class to use (e.g., "article", "report").
- `packages` (`dict[str, str]`): Dictionary of LaTeX packages and options.


- `__eq__()`
  Return self==value.


- `__init__()`
  Initialize self.  See help(type(self)) for accurate signature.


- `__repr__()`
  Return repr(self).


### `beauti_tex.proj_builder`


LaTeX project generation for beauti-tex.

This module provides functionality to create a fully structured LaTeX
project for academic papers. It builds the required directory layout,
copies template files, and generates initial `.tex` sources based on
a user-provided configuration.

Typical usage example:

  from beauti_tex.projBuilder import make_project

  make_project(
  projName="MyPaper",
  projPath=Path("~/papers").expanduser(),
  cfgPath=Path("config.ini"),
  )


#### `make_project()`


Creates a basic LaTeX Project for academic papers
**Args:**
- `proj_name` (`str`): Name of the project / main folder.

- `proj_path` (`Path |str| None`): Optional base directory. Default is the current working directory.

- `cfg_path` (`Path |str| None`): Optional path to a configuration INI file.
**Raises:**
  FileExistsError: If the project folder already exists.

  FileNotFoundError: If template files are not found

Example:

  >>> make_project("MyPaper")


### `beauti_tex.utils`


This module contains general utility functions that can be reused
across different parts of the project.

Included functions:
- safe_name(name: str) -> str
  Converts a given name into a safe format suitable for filenames,
  variable names, etc.


Examples:
>>> from utils import safe_name
>>> safe_name("my file")
'my_file'

Notes:
- All functions are independent and can be used individually.
- Importing this module does not produce any side effects.


#### `safe_name()`


Secure a valid folder name.

Rules:
- No spaces (converted to underscores)
- Cannot contain any of: <>:"/\|?*
- Cannot end with a dot
- Cannot be empty
**Args:**
- `name` (`str`): Name to check.
**Returns:**
  str: validated name.


## License


Apache-2.0
