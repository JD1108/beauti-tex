from pathlib import Path
import configparser
from dataclasses import dataclass

@dataclass
class Config:
    folders: list[str]
    chapters: list[str]
    style: str
    tempPath: Path
    size:int
    clas:str
    packages: dict[str, str]

def getConfig(path:Path |None=None)->Config:
    config = configparser.ConfigParser()
    defFile = Path(__file__).parent / "default.ini"
    if not defFile.exists():
        raise FileNotFoundError(f"{defFile} not found!")
    config.read(defFile)
    if path:
        if not path.exists():
            raise FileNotFoundError(f"{path} not found!")
        config.read(path)
    folders=[x.strip() for x in config['project']['folders'].split(',')]
    chapters = [x.strip() for x in config['project']['chapters'].split(',')]
    style = config['project']['style']
    tempPath = Path(config['project']['templates'])
    if not tempPath.is_absolute():
        tempPath=Path(__file__).parent / tempPath
    if not tempPath.exists():
        raise FileNotFoundError(f"{tempPath} not found!")
    size = config.getint('project', 'size')
    clas = config['project']['clas']
    packages = dict(config['packages'])
    return Config(folders,chapters,style,tempPath,size,clas,packages)