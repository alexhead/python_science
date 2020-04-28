import xlrd, xlwt

rb = xlrd.open_workbook('./files/tab.xlsx')

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем значение первой ячейки A1
val = sheet.row_values(0)[0]

#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

print(*vals[8])