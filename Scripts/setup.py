import sys
from cx_Freeze import setup, Executable

include_files = ['README.txt', 'Templates', 'tcl86t.dll', 'tk86t.dll', 'makeDuct.py', 'formatExl.py']

build_exe_options = {"packages": ["os"], "includes": ["tkinter"],
                     "include_files": include_files}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ProExl",
        version = "0.0.1",
        description = "Write HVAC Database Items to Excel",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ProExl.py", base=base)])
