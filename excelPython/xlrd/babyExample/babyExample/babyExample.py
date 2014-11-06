import xlrd

excelFile = "data/someData.xlsx"

workbook = xlrd.open_workbook(excelFile)
sheet = workbook.sheet_by_index(0)

#shove it in a list to make it easier
data = [[sheet.cell_value(r,col)
         for col in range(sheet.ncols)]
            for r in range(sheet.nrows)]


print data[0][0]