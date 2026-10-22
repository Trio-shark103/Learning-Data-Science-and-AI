import openpyxl

# Create a new Workbook
wb = openpyxl.Workbook()

# Select the active sheet
sheet = wb.active

# Merge cells from A1 to B2
sheet.merge_cells("A1:B2")

# Write data in the merged cell
sheet["A1"] = "Merged Cells"

# Save the workbook
wb.save("merged_workbook.xlsx")





