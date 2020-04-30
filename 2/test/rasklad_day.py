import xlrd
import math
from itertools import groupby

def catalog_func(value_1):
    x = {}
    for i in range(sheet_1.nrows-1):
        x[sheet_1.row_values(i + 1)[0]] = sheet_1.row_values(i + 1)[value_1]
    return x

def energy_sum (energy_dict, x_range, y_range):
    a = 0
    for i in range(x_range, y_range):
        a += energy_dict[sheet_2.row_values(i+1)[1]]*sheet_2.row_values(i+1)[2]*0.01
    a = math.floor(a)
    return a

catalog = xlrd.open_workbook('../files/trekking3.xlsx')
sheet_1 = catalog.sheet_by_index(0)
rasklad = xlrd.open_workbook('../files/trekking3.xlsx')
sheet_2 = rasklad.sheet_by_index(1)

# ККАЛ
calories_dict = catalog_func(1)
#БЕЛОК
protein_dict = catalog_func(2)
#ЖИРЫ
fat_dict = catalog_func(3)
#УГЛЕВОДЫ
carbohydrates_dict = catalog_func(4)

day_spis = []
for i in range(sheet_2.nrows-1):
    day_spis.append(sheet_2.row_values(i+1)[0])
print(day_spis)
day_count = [el for el, _ in groupby(day_spis)]
print(day_count)
day_range = []
for i in range(len(day_count)):
    day_index = day_spis.index(day_count[i])
    day_range.append(day_index)
print(day_range)

for i in range(len(day_range)-1):
    #print(day_range[i], day_range[i+1])
    #подсчитываем сумму калорий
    calories_sum = energy_sum(calories_dict, day_range[i], day_range[i+1])
    #подсчитываем сумму белков
    protein_sum = energy_sum(protein_dict, day_range[i], day_range[i+1])
    #подсчитываем сумму жиров
    fat_sum = energy_sum(fat_dict, day_range[i], day_range[i+1])
    #подсчитываем сумму углеводов
    carbohydrates_sum = energy_sum(carbohydrates_dict, day_range[i], day_range[i+1])

    print(calories_sum, protein_sum, fat_sum, carbohydrates_sum)

calories_sum = energy_sum(calories_dict, 95, len(day_spis))
    #подсчитываем сумму белков
protein_sum = energy_sum(protein_dict, 95, len(day_spis))
    #подсчитываем сумму жиров
fat_sum = energy_sum(fat_dict, 95, len(day_spis))
    #подсчитываем сумму углеводов
carbohydrates_sum = energy_sum(carbohydrates_dict, 95, len(day_spis))

print(calories_sum, protein_sum, fat_sum, carbohydrates_sum)



