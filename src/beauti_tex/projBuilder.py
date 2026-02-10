from pathlib import Path
from .config import getConfig
import shutil

def projBuilder(projName:str,*,projPath:Path |None=None,cfgPath:Path|None=None)->None:
    """
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
    """

    cfg = getConfig(cfgPath)
    #folders
    if projPath is None:
        projPath=Path.cwd()/projName
    if projPath.exists():
        raise FileExistsError(f"{projPath} already exists!")
    for folder in cfg.folders:
        path = projPath/folder
        path.mkdir(parents=True)
    #files
    #main.tex
    main=(cfg.tempPath/"main.tex").read_text()
    main=main.replace("<<SIZE>>",f"{cfg.size}")
    main=main.replace("<<CLAS>>",cfg.clas)
    chapters = [f"\\input{{chapters/{c}}}" for c in cfg.chapters]
    chapters="\n".join(chapters)
    main=main.replace("<<CHAPTERS>>",chapters)
    (projPath/"main.tex").write_text(main)

    #chapters
    (projPath/"chapters").mkdir(parents=True, exist_ok=True)
    for file in cfg.chapters:
        (projPath /"chapters"/ f"{file}.tex").write_text(f"\\chapter{{{file.capitalize()}}}")

    #other
    texs = ["pak.tex", "literature.bib","chapters/appendix.tex"]
    for tex in texs:
        (projPath / tex).touch()

    (projPath / "chapters" / "abstract.tex").write_text(r"\begin{abstract}"+"\n\n"+r"\end{abstract}")
    shutil.copy(cfg.tempPath/"titlepage.tex",projPath/"chapters"/"titlepage.tex")
    print("Latex Project Created!")


