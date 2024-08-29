from pathlib import Path
import re

def list_all_files_in_dir(dir: str) -> list:
    """list_all_files_in_dir This function will return a list of all the filenames
    that are present in the a given directory "dir". Names of sub-directories and the files
    within those sub-directories are ignored.

    Parameters
    ----------
    dir : str
        Path that points to a directory

    Returns
    -------
    list
        A list of filenames
    """
    return [item for item in Path(dir).iterdir() if item.is_file()]

def remove_leading_underscore(s: str) -> str:
    if s and s[0] == '_':
        return s[1:]
    return s

def is_hex_color(string):
    pattern = r"^#[0-9A-Fa-f]{6}$" # The regex pattern definition for a hex color
    return bool(re.match(pattern, string))
