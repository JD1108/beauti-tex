"""
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
"""


from pathlib import Path
import configparser
from dataclasses import dataclass

@dataclass
class Config:
    """
    Dataclass representing the configuration for a LaTeX project.

    Attributes:
        folders (list[str]): List of folder names to create in the project.
        chapters (list[str]): List of chapter filenames to generate.
        style (str): Document style or template identifier.
        temp_path (Path): Path to template files for project generation.
        size (int): Paper size (e.g., 10, 11, 12 pt).
        clas (str): LaTeX class to use (e.g., "article", "report").
        packages (dict[str, str]): Dictionary of LaTeX packages and options.
    """
    folders: list[str]
    chapters: list[str]
    style: str
    temp_path: Path
    size:int
    clas:str
    packages: dict[str, str]

def get_config(path:Path | str |None=None)->Config:
    """
    Load and parse the configuration for a LaTeX project.

    Reads default settings from `default.ini` located in the same directory
    as this module. If an optional user configuration file is provided,
    its settings override the defaults.

    Args:
        path (Path | str | None): Optional path to a user-provided configuration INI file.

    Returns:
        Config: A populated Config dataclass instance with all project settings.

    Raises:
        FileNotFoundError: If the default INI file or the user-provided file does not exist,
                           or if the template directory does not exist.
    """
    config = configparser.ConfigParser()
    def_file = Path(__file__).parent / "default.ini"
    if not def_file.exists():
        raise FileNotFoundError(f"{def_file} not found!")
    config.read(def_file)

    if path:
        if path == "":
            raise ValueError("Path must not be an empty string.")
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"{path} not found!")
        config.read(path)
    folders=[x.strip() for x in config['project']['folders'].split(',')]
    chapters = [x.strip() for x in config['project']['chapters'].split(',')]
    style = config['project']['style']
    temp_path = Path(config['project']['templates'])
    if not temp_path.is_absolute():
        temp_path=Path(__file__).parent / temp_path
    if not temp_path.exists():
        raise FileNotFoundError(f"{temp_path} not found!")
    size = config.getint('project', 'size')
    clas = config['project']['clas']
    packages = dict(config['packages'])
    return Config(folders,chapters,style,temp_path,size,clas,packages)