import xlrd

excelFile = "data/someData.xlsx"

workbook = xlrd.open_workbook(excelFile)
sheet = workbook.sheet_by_index(0)

print sheet.cell_value(2,0)
