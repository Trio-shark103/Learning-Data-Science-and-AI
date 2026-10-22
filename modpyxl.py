from openpyxl import Workbook
from openpyxl.styles import Font # font styles

#formatting cells in a workbook
wb = Workbook()
sheet = wb.active

sheet["A1"] = "Formatted Text"
sheet["A1"].font = Font(size=14, bold=True, color="FF0000")

wb.save("formatted_workbook.xlsx")