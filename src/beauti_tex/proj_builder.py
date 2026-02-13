
"""
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

"""

from pathlib import Path
from .config import get_config
from .utils import safe_name
import shutil
import os


def make_project(proj_name:str,*,proj_path:Path|str |None=None,cfg_path:Path|str|None=None)->None:
    """
    Creates a basic LaTeX Project for academic papers

    Args:

        proj_name (str): Name of the project / main folder.

        proj_path (Path |str| None): Optional base directory. Default is the current working directory.

        cfg_path (Path |str| None): Optional path to a configuration INI file.

    Raises:

        FileExistsError: If the project folder already exists.

        FileNotFoundError: If template files are not found

    Example:

        >>> make_project("MyPaper")
    """
    proj_name=safe_name(proj_name)

    cfg = get_config(cfg_path)
    #folders
    if proj_path is None:
        proj_path=Path.cwd()/proj_name
    elif isinstance(proj_path,str):
        proj_path=Path(proj_path)/proj_name
    else:
        proj_path=proj_path/proj_name
    if proj_path.exists():
        raise FileExistsError(f"{proj_path} already exists!")
    if not os.access(proj_path.parent, os.W_OK):
        raise PermissionError(f"No write permission in {proj_path}!")
    for folder in cfg.folders:
        path = proj_path/folder
        path.mkdir(parents=True)
    #files
    #main.tex
    main=(cfg.temp_path/"main.tex").read_text()
    main=main.replace("<<SIZE>>",f"{cfg.size}")
    main=main.replace("<<CLAS>>",cfg.clas)
    chapters = [f"\\input{{chapters/{c}}}" for c in cfg.chapters]
    chapters="\n".join(chapters)
    main=main.replace("<<CHAPTERS>>",chapters)
    (proj_path/"main.tex").write_text(main)

    #chapters
    (proj_path/"chapters").mkdir(parents=True, exist_ok=True)
    for file in cfg.chapters:
        (proj_path /"chapters"/ f"{file}.tex").write_text(f"\\chapter{{{file.capitalize()}}}")

    #other
    texs = ["pak.tex", "literature.bib","chapters/appendix.tex"]
    for tex in texs:
        (proj_path / tex).touch()

    (proj_path / "chapters" / "abstract.tex").write_text(r"\begin{abstract}"+"\n\n"+r"\end{abstract}")
    shutil.copy(cfg.temp_path/"titlepage.tex",proj_path/"chapters"/"titlepage.tex")
    print("Latex Project Created!")


