import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = 10
sheet["A2"] = 20
sheet["A3"] = "=A1 + A2"  # Formula

wb.save("formula_workbook.xlsx")