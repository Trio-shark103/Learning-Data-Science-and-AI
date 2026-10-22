# import necessary library
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Create a new Workbook
wb = Workbook()
ws = wb.active

# Add data to the worksheet
data = [
    ["Year", "Sales"],
    [2020, 300],
    [2021, 400],
    [2022, 350],
    [2023, 500],
]

for row in data:
    ws.append(row)

# Create a BarChart object
chart = BarChart()

# Define the data (sales values) for the chart
data = Reference(ws, min_col=2, min_row=1, max_row=5)

# Define the categories (years)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)

# Add data and categories to the chart
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# Add the chart to the worksheet
ws.add_chart(chart, "E5")

# Save the Workbook to a file
wb.save("sales_chart.xlsx")