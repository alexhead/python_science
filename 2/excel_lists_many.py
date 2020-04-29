import xlrd, xlwt

rb = xlrd.open_workbook('./files/tab.xlsx')

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем значение первой ячейки A1
val = sheet.row_values(0)[0]

#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]



for i in range(7, len(vals)):
    row = vals[i]
    name = row[0]
    grades = row[1]
    if name not in results:
        results[name] = {}
    for j in range(len(subjects)):
        results[name][subjects[j] + '7'] = grades[j]
    print(name)
    print(grades)
    #print(row)
#print(subjects)
