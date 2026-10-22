from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series

# Create a new Workbook
wb = Workbook()
ws = wb.active

# Add data to the worksheet
data = [
    ["X", "Y1", "Y2"],
    [1, 10, 20],
    [2, 20, 30],
    [3, 30, 40],
    [4, 40, 50],
    [5, 50, 60],
]

for row in data:
    ws.append(row)

# Create a ScatterChart object
chart = ScatterChart()
chart.title = "Scatter Chart Example"
chart.style = 13
chart.x_axis.title = 'X Axis'
chart.y_axis.title = 'Y Axis'

# Define the X and Y data for the first series
x_values = Reference(ws, min_col=1, min_row=2, max_row=6)
y_values = Reference(ws, min_col=2, min_row=2, max_row=6)
series1 = Series(y_values, x_values, title="Y1 Series")

# Define the Y data for the second series
y_values2 = Reference(ws, min_col=3, min_row=2, max_row=6)
series2 = Series(y_values2, x_values, title="Y2 Series")

# Add the series to the chart
chart.series.append(series1)
chart.series.append(series2)

# Add the chart to the worksheet
ws.add_chart(chart, "E5")

# Save the Workbook to a file
wb.save("scatter_chart.xlsx")