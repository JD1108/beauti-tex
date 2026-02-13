"""
test_config.py

Tests for the beauti_tex configuration module.
Ensures that get_config correctly reads default and user-provided INI files,
parses the settings, and populates the Config dataclass.
"""

import pytest
from pathlib import Path
import shutil
from beauti_tex import config as bt_config

@pytest.fixture
def tmp_ini(tmp_path):
    """
    Creates a temporary INI file for testing purposes.
    """
    ini_file = tmp_path / "test.ini"
    ini_file.write_text(
        """
[project]
folders = folder1, folder2
chapters = chap1, chap2
style = fancy
templates = templates
size = 12
clas = article

[packages]
geometry = margin=1in
babel = english
"""
    )
    # Create templates folder so get_config does not raise FileNotFoundError
    folder = tmp_path / "templates"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir()
    return ini_file

def test_get_config_default(tmp_path):
    """Test loading the default INI configuration."""
    default_ini = tmp_path / "default.ini"
    default_ini.write_text(
        """
[project]
folders = f1,f2
chapters = c1,c2
style = simple
templates = temp
size = 11
clas = report

[packages]
hyperref = colorlinks=True
"""
    )
    # Create templates folder
    folder = tmp_path / "temp"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir()

    # Patch __file__ temporarily for relative paths
    original_file = bt_config.__file__
    bt_config.__file__ = str(tmp_path / "dummy.py")

    cfg = bt_config.get_config()

    # Restore original __file__ to avoid side effects
    bt_config.__file__ = original_file

    assert cfg.folders == ["f1", "f2"]
    assert cfg.chapters == ["c1", "c2"]
    assert cfg.style == "simple"
    assert cfg.size == 11
    assert cfg.clas == "report"
    assert cfg.packages == {"hyperref": "colorlinks=True"}
    assert cfg.temp_path.exists() is True

def test_get_config_user(tmp_ini, tmp_path):
    """Test loading a user-provided INI overrides defaults."""
    default_ini = tmp_path / "default.ini"
    default_ini.write_text(
        """
[project]
folders = f_default
chapters = c_default
style = default
templates = default_temp
size = 10
clas = article

[packages]
"""
    )
    # Create templates folder referenced in user INI
    folder = tmp_path / "templates"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir()

    original_file = bt_config.__file__
    bt_config.__file__ = str(tmp_path / "dummy.py")

    cfg = bt_config.get_config(tmp_ini)

    bt_config.__file__ = original_file

    assert cfg.folders == ["folder1", "folder2"]
    assert cfg.chapters == ["chap1", "chap2"]
    assert cfg.style == "fancy"
    assert cfg.size == 12
    assert cfg.clas == "article"
    assert cfg.packages == {"geometry": "margin=1in", "babel": "english"}
    assert cfg.temp_path.exists() is True