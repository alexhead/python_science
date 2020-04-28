import xlrd, xlwt
from statistics import median
import operator
import pandas as pd
import statistics

rb = xlrd.open_workbook('../files/salaries.xlsx')

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

# Ищем регион с самой высокой мед. зарплатой
dict_avg_work = {}
for i in range(sheet.nrows-1):
    subjects = (vals[i+1][0])
    median_work = median(vals[i+1][1:])
    dict_avg_work[subjects] = median_work

a = max(dict_avg_work.items(), key=operator.itemgetter(1))[0]

# Ищем профессию с зарплатой (Pandas)
df = pd.read_excel('../files/salaries.xlsx')
spis_prof = sheet.row_values(0) #список профессий с 1
dict_avg_prof = {}
for i in range(len(spis_prof)-1):
    sys_name_lst = df.iloc[:, i+1].tolist()
    avg = statistics.mean(sys_name_lst)
    dict_avg_prof[spis_prof[i+1]] = avg
b = max(dict_avg_prof.items(), key=operator.itemgetter(1))[0]

# Ответ:
print(a, b)




