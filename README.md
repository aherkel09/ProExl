# ProExl
Using Python to write HVAC ductwork items to Excel for insertion into a ProEst Estimating database.

## Overview:
- ProExl.py creates a user interface which prompts users to choose a duct type and enter a size range.
- makeDuct.py generates duct objects from user requests.
- formatExl.py formats data from duct objects and inserts them into an excel sheet.
- setup.py uses cx\_Freeze to create an executable file from ProExl.py and includes other file resources.
- Templates/RevisionNum.txt tracks database revisions by appending the date and time of each duct generation.
- Templates/sampleData.xlsx is the excel template from which column headers are read. It is formatted for a ProEst Estimating database.

## Modules/Libraries Used:
- [Python 3][py_link]: Python is an interpreted high-level programming language for general-purpose programming.
- [openpyxl][opxl_link]: A Python library to read/write Excel 2010 xlsx/xlsm files.
- [tkinter][tk_link]: Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of   Tcl/Tk.
- [datetime][dt_link]: The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
- [cx\_Freeze][cx_link]: A set of scripts and modules for freezing Python scripts into executables.

## Instructions:
Note: You must have [Python 3][py_link] installed in order to build ProExl yourself. If you would like to use the fully assembled software, download the ProExl zip file and open ProExl.exe.
1. Download the files in the Scripts folder and the Templates folder. Be sure that the directory structure in the destination folder matches the directory structure on Github.
2. Copy the tcl8.6t.dll and tk8.6t.dll files from your DLLs folder (`C:\Users\<username>\AppData\Local\Programs\Python\Python3<x>\DLLs`) and paste them in the Scripts folder.
3. Open a command prompt, navigate to the Scripts folder and use setup.py to create an executable file for the project. On Windows, run the following commands:
```
set TCL_LIBRARY=C:\Users\<username>\AppData\Local\Programs\Python\Python3<x>\tcl\tcl8.6
set TK_LIBRARY=C:\Users\<username>\AppData\Local\Programs\Python\Python3<x>\tcl\tk8.6
python setup.py bdist_msi
```
(If you are using Mac OS or Linux, consult the [cx\_Freeze Documentation][cx_link])

4. Create a shortcut to ProExl.exe or pin it to the start menu for easy access.
5. Run the program, follow the prompts and enjoy!

### If you experience any issues with the software, please contact me via the email on my Github profile.

[py_link]: https://docs.python.org/3/tutorial/
[opxl_link]: https://openpyxl.readthedocs.io/en/stable/
[tk_link]: https://wiki.python.org/moin/TkInter
[dt_link]: https://docs.python.org/3/library/datetime.html
[cx_link]: http://cx-freeze.readthedocs.io/en/latest/index.html
