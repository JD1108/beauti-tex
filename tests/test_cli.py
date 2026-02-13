"""
Tests for the beauti_tex CLI.
"""

import sys
from pathlib import Path
import pytest
from beauti_tex import cli
from beauti_tex.proj_builder import make_project


@pytest.fixture
def config_fixture(tmp_path):
    """
    Creates a minimal Config object and template folder for testing CLI.
    """
    template = tmp_path / "template"
    template.mkdir()
    (template / "main.tex").write_text("<<CLAS>> document class, size <<SIZE>>\n<<CHAPTERS>>")
    (template / "titlepage.tex").write_text("TITLE PAGE")

    from beauti_tex.config import Config
    return Config(
        folders=["figures", "tables"],
        chapters=["intro", "methods"],
        style="fancy",
        temp_path=template,
        size=12,
        clas="report",
        packages={"geometry": "margin=1in"}
    )


def test_make_project_cli(tmp_path, config_fixture, monkeypatch, capsys):
    """
    Test CLI command 'make-project'.
    """
    # Patch get_config to return our fixture
    monkeypatch.setattr("beauti_tex.proj_builder.get_config", lambda path=None: config_fixture)

    # Simulate CLI arguments
    proj_name = "MyCLITest"
    test_args = [
        "prog",  # dummy argv[0]
        "make-project",
        "--name", proj_name,
        "--project-path", str(tmp_path),
        "--config-path", str(tmp_path / "dummy.ini")  # won't be used due to patch
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    # Call main
    cli.main()

    # Check project folder created
    proj_dir = tmp_path / proj_name
    assert proj_dir.exists()

    # Check subfolders
    for folder in config_fixture.folders:
        assert (proj_dir / folder).exists()
    assert (proj_dir / "chapters").exists()

    # Check main.tex content
    main_tex = (proj_dir / "main.tex").read_text()
    assert "report document class" in main_tex
    assert "size 12" in main_tex
    for chapter in config_fixture.chapters:
        assert f"\\input{{chapters/{chapter}}}" in main_tex

    # Check other files
    for file in ["pak.tex", "literature.bib", "chapters/appendix.tex",
                 "chapters/abstract.tex", "chapters/titlepage.tex"]:
        assert (proj_dir / file).exists()