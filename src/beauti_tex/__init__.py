"""
Beauti-tex package initializer.

This module exposes the main public API for beauti-tex, including
project creation and configuration management.

Public API:
    - make_project: Create a structured LaTeX project.
    - Config: Dataclass representing project configuration.
    - get_config: Load configuration from INI files.

Version:
    0.1.0
"""

__version__ = "0.1.0"

from .proj_builder import make_project
from .config import Config, get_config

__all__=["make_project","Config","get_config"]