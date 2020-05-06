import xmltodict
import urllib.request

destination = '../files/map_my.osm'
url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
urllib.request.urlretrieve(url, destination)

fin = open('../files/map_my.osm', 'r', encoding='utf-8')

text = fin.read()
fin.close()
shops = 0
dct = xmltodict.parse(text)
tag_yes = 0
tag_no = 0
for node in dct['osm']['node']:
     if 'tag' in node:
          tag_yes += 1
     else:
          tag_no += 1
print(tag_yes, tag_no)

