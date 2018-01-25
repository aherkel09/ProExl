# ProExl
Using Python to write HVAC ductwork items to Excel for insertion into a ProEst Estimating database.

## Overview:
- ProExlGUI.py creates a user interface which prompts users to choose a duct type and enter a size range.
- makeDuct.py generates duct objects from user requests.
- formatExl.py formats data from duct objects and inserts them into an excel sheet.

## Modules/Libraries Used:
- [python3][py_link]: Python is an interpreted high-level programming language for general-purpose programming.
- [openpyxl][opxl_link]: A Python library to read/write Excel 2010 xlsx/xlsm files.
- [tkinter][tk_link]: Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of   Tcl/Tk.
- [datetime][dt_link]: The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
- [cx\_Freeze][cx_link]: A set of scripts and modules for freezing Python scripts into executables.

## Instructions:
1. Download the files in the Scripts folder and the Templates folder. Be sure that the directory structure in the destination folder matches the directory structure on Github.
2. Open a command prompt, navigate to the Scripts folder and use cx\_Freeze to create an executable file for the project. On Windows, run the following commands:
```
set TCL_LIBRARY=C:\Users\username\AppData\Local\Programs\Python36-32\tcl\tcl8.6
set TK_LIBRARY=C:\Users\username\AppData\Local\Programs\Python36-32\tcl\tk8.6
python setup.py bdist_msi
```
(If you are using Mac OS or Linux, consult the [cx\_Freeze Documentation][cx_link])
3. Create a shortcut to ProExl.exe or pin it to the start menu for easy access.
4. Run the program, follow the prompts and enjoy!

### If you experience any issues with the software, please contact me via my email on my Github profile.

[py_link]: https://docs.python.org/3/tutorial/
[opxl_link]: https://openpyxl.readthedocs.io/en/stable/
[tk_link]: https://wiki.python.org/moin/TkInter
[dt_link]: https://docs.python.org/3/library/datetime.html
[cx_link]: http://cx-freeze.readthedocs.io/en/latest/index.html
