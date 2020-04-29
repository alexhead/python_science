import xlrd
import math

catalog = xlrd.open_workbook('../files/trekking1.xlsx')
sheet_1 = catalog.sheet_by_index(0)
rasklad = xlrd.open_workbook('../files/trekking2.xlsx')
sheet_2 = rasklad.sheet_by_index(1)

# ККАЛ
calories_dict = {}
for i in range(sheet_1.nrows-1):
    calories_dict[sheet_1.row_values(i+1)[0]] = sheet_1.row_values(i+1)[1]

#БЕЛОК
protein_dict = {}
for i in range(sheet_1.nrows-1):
    protein_dict[sheet_1.row_values(i+1)[0]] = sheet_1.row_values(i+1)[2]

#ЖИРЫ
fat_dict = {}
for i in range(sheet_1.nrows-1):
    fat_dict[sheet_1.row_values(i+1)[0]] = sheet_1.row_values(i+1)[3]

#УГЛЕВОДЫ
carbohydrates_dict = {}
for i in range(sheet_1.nrows-1):
    carbohydrates_dict[sheet_1.row_values(i+1)[0]] = sheet_1.row_values(i+1)[4]

#подсчитываем сумму калорий
calories_sum = 0
for i in range(sheet_2.nrows-1):
    calories_sum += calories_dict[sheet_2.row_values(i+1)[0]]*sheet_2.row_values(i+1)[1]*0.01
calories_sum = math.floor(calories_sum)

#подсчитываем сумму белков
protein_sum = 0
for i in range(sheet_2.nrows-1):
    protein_sum += protein_dict[sheet_2.row_values(i+1)[0]]*sheet_2.row_values(i+1)[1]*0.01
protein_sum = math.floor(protein_sum)

#подсчитываем сумму жиров
fat_sum = 0
for i in range(sheet_2.nrows-1):
    fat_sum += fat_dict[sheet_2.row_values(i+1)[0]]*sheet_2.row_values(i+1)[1]*0.01
fat_sum = math.floor(fat_sum)

#подсчитываем сумму углеводов
carbohydrates_sum = 0
for i in range(sheet_2.nrows-1):
    if type(carbohydrates_dict[sheet_2.row_values(i+1)[0]]) == str:
        carbohydrates_dict[sheet_2.row_values(i+1)[0]] = float(0)
    carbohydrates_sum += carbohydrates_dict[sheet_2.row_values(i+1)[0]]*sheet_2.row_values(i+1)[1]*0.01
carbohydrates_sum = math.floor(carbohydrates_sum)

print(calories_sum, protein_sum, fat_sum, carbohydrates_sum)



