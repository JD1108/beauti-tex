# Changelog

All notable changes to `beauti-tex` are documented here.  

## [0.1.0] - 2026-02-13
### Added
- `utils` module with `safe_name` function to remove unallowed names
- CLI using argparse:
  - `make-project` command with `--name`, `--project-path`, and `--config-path` options
- Editable installation (`pip install -e .`) supported
- pytest test cases for:
    -`utils`
    -`config`
    -`proj_builder`
    -`cli` 
- CHANGELOG.md
- GitHub connection
- String support for `proj_builder` and `get_config`

### Changed
- CamelCase naming in modules and functions adjusted
---

## [0.1.0a3] - 2026-02-09
### Added
- First alpha release with basic LaTeX project generation.
- `make_project` function:
  - Creates project folder and subfolders
  - Generates `main.tex` with chapters
  - Adds standard files like `pak.tex`, `literature.bib`, and `appendix.tex`
  - Copies `titlepage.tex` from the template directory

- `Config` dataclass and `get_config()`:
  - Reads defaults from `default.ini`
  - Supports optional user configuration


### Changed
- Project structure moved to `src/beauti_tex/`


### Fixed
- Import issues during testing due to venv/pip misconfiguration
- Paths for templates and project files corrected

---
