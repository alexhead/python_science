import re
import sys
import requests

def func_del_pair(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def sort_dictionary_by_value(dictionary):
    list_of_sorted_pairs = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key=dictionary.get, reverse=True)]
    # Так мы создаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # "reverse = False" говорит, что перебор нужно делать в обычном порядке
    # Если нужно отсортировать значения в обратном порядке, то reverse можно сделать = True
    return list_of_sorted_pairs # после сделанных операций возвращаем получившийся список

res = requests.get(str("https://stepik.org/media/attachments/lesson/209719/2.html"))
spis = []

codes_pair = dict()

with open("stroki.html", "wb") as f:
    f.write(res.content)

f = open("stroki.html")

for line in f:
    line = line.rstrip()
    pattern = r'<code>\w*</code>'
    all_inclusions = re.findall(pattern, line)
    print(all_inclusions)
    spis += all_inclusions

spis_change = func_del_pair(spis)
#print(spis)
#print(spis_change)

for name in spis_change:
    i = 0
    for spi in spis:
        if spi == name:
            i += 1
    codes_pair[name] = i

print(codes_pair)

new_codes_pair = sort_dictionary_by_value(codes_pair)

for x in new_codes_pair:
    print(x[0], x[1])