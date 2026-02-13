"""
test_proj_builder.py

Tests for the beauti_tex.proj_builder.make_project function.
"""

import pytest
from pathlib import Path
import shutil
from beauti_tex.proj_builder import make_project
from beauti_tex.config import Config
from beauti_tex.config import get_config

@pytest.fixture
def tmp_template(tmp_path):
    """
    Creates a minimal template folder with required files.
    """
    template = tmp_path / "template"
    if template.exists():
        shutil.rmtree(template)
    template.mkdir()
    # main.tex with placeholders
    (template / "main.tex").write_text(
        "<<CLAS>> document class, size <<SIZE>>\n<<CHAPTERS>>"
    )
    # titlepage.tex
    (template / "titlepage.tex").write_text("TITLE PAGE")
    return template

@pytest.fixture
def config_fixture(tmp_template):
    """
    Returns a Config object pointing to the tmp_template.
    """
    return Config(
        folders=["figures", "tables"],
        chapters=["intro", "methods"],
        style="fancy",
        temp_path=tmp_template,
        size=12,
        clas="report",
        packages={"geometry": "margin=1in"}
    )

def test_make_project(tmp_path, config_fixture, monkeypatch):
    """
    Test that make_project correctly creates folders and files.
    """
    proj_name = "TestPaper"
    proj_dir = tmp_path / proj_name
    if proj_dir.exists():
        shutil.rmtree(proj_dir)

    # Patch get_config to return our fixture
    monkeypatch.setattr("beauti_tex.proj_builder.get_config", lambda path=None: config_fixture)

    make_project(proj_name, proj_path=tmp_path)

    # Check main project folder exists
    assert proj_dir.exists()
    # Check subfolders
    for folder in config_fixture.folders:
        assert (proj_dir / folder).exists()
    assert (proj_dir / "chapters").exists()

    # Check main.tex created and placeholders replaced
    main_tex = (proj_dir / "main.tex").read_text()
    assert "report document class" in main_tex
    assert "size 12" in main_tex
    for chapter in config_fixture.chapters:
        assert f"\\input{{chapters/{chapter}}}" in main_tex

    # Check chapter files exist
    for chapter in config_fixture.chapters:
        assert (proj_dir / "chapters" / f"{chapter}.tex").exists()

    # Check other files
    for file in ["pak.tex", "literature.bib", "chapters/appendix.tex", "chapters/abstract.tex", "chapters/titlepage.tex"]:
        assert (proj_dir / file).exists()