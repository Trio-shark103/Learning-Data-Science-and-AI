from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

# Create a new Workbook
wb = Workbook()
ws = wb.active

# Add data to the worksheet
data = [
    ["Category", "Value"],
    ["A", 40],
    ["B", 30],
    ["C", 20],
    ["D", 10],
]

for row in data:
    ws.append(row)

# Create a PieChart object
chart = PieChart()

# Define the data (values) for the chart
data = Reference(ws, min_col=2, min_row=2, max_row=5)

# Define the categories (labels)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)

# Add data and categories to the chart
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# Add the chart to the worksheet
ws.add_chart(chart, "E5")

# Save the Workbook to a file
wb.save("category_pie_chart.xlsx")