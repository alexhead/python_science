import xlrd, xlwt
import requests
import tempfile, os, zipfile

def sort_dictionary_by_value(dictionary):
    list_of_sorted_pairs = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key=dictionary.get, reverse=False)]
    # Так мы создаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # "reverse = False" говорит, что перебор нужно делать в обычном порядке
    # Если нужно отсортировать значения в обратном порядке, то reverse можно сделать = True
    return list_of_sorted_pairs # после сделанных операций возвращаем получившийся список

#response = requests.get('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip')
#file = tempfile.TemporaryFile()
#file.write(response.content)
#fzip = zipfile.ZipFile(file)
#fzip.extractall('../files/rogaikopyta/')
#file.close()
#fzip.close()


work_man = {}
for i in range(1, 1001):
    catalog = xlrd.open_workbook('../files/rogaikopyta/'+str(i)+'.xlsx')
    sheet = catalog.sheet_by_index(0)
    name = sheet.row_values(1)[1]
    money = sheet.row_values(1)[3]
    work_man[name] = money
new = sorted(work_man)

#создем книгу
wb = xlwt.Workbook()
ws = wb.add_sheet('Test')

#в столбец B запишем нашу последовательность из столбца A исходного файла
i = 0
for i in range(len(new)):
    ws.write(i, 0, new[i])
    ws.write(i, 1, int(work_man[new[i]]))
    i =+ i
#сохраняем рабочую книгу
wb.save('../files/roga_full.xlsx')