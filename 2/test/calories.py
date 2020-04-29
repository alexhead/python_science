import xlrd, xlwt
import collections

rb = xlrd.open_workbook('../files/trekking1.xlsx')

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем значение первой ячейки A1
val = sheet.row_values(1)[0]

#создаем словарь продукт - ккал
dict_1 = {}
for i in range(sheet.nrows-1):
    dict_1[sheet.row_values(i+1)[0]] = sheet.row_values(i+1)[1]
dict_1_sort = collections.OrderedDict(sorted(dict_1.items())) #сортируем ключи в алфавитном порядке

# находим все значения и сортируем в порядке убывания "ккал"
value_spis = []
for key, value in dict_1.items():
    value_spis.append(value)
sorted_value_spis = sorted(value_spis, reverse=True)
print(sorted_value_spis)

# получаем ключ по значению и удаляем из словаря, чтобы найти следующее
for i in range(len(sorted_value_spis)):
    final_products = get_key(dict_1_sort, sorted_value_spis[i])
    print(final_products)
    del dict_1_sort[final_products]





