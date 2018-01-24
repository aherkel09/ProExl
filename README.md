# ProExl
Using Python to write HVAC ductwork items to Excel for insertion into a ProEst Estimating database.

## Overview:
- ProExlGUI.py creates a user interface which prompts users to choose a duct type and enter a size range.
- insert\_duct.py generates duct objects from user requests.
- formatxl.py formats data from duct objects and inserts them into an excel sheet.

## Modules/Libraries Used:
- openpyxl: A Python library to read/write Excel 2010 xlsx/xlsm files.
- datetime: The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
