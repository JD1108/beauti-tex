"""
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
"""

def safe_name(name:str)->str:
    """
    Secure a valid folder name.

    Rules:
    - No spaces (converted to underscores)
    - Cannot contain any of: <>:"/\|?*
    - Cannot end with a dot
    - Cannot be empty

    Args:
        name (str): Name to check.

    Returns:
        str: validated name.
    """

    if name == "":
        name="empty"
    # remove invalid characters
    err=r'[<>:"/\\|?*]'
    for e in err:
        name=name.replace(e,'_')
    #remove spaces
    name=name.replace(' ','_')

    #remove dots in beginning and end
    if name[0]=='.':
        name=name[1:]
    if name[-1]=='.':
        name=name[:-1]+'_'
    return name

