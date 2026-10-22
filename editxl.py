import openpyxl

wb = openpyxl.load_workbook("sample_work.xlsx")
sheet = wb.active

sheet["B2"] = 26  # Update age

wb.save("sample_work_modified.xlsx")