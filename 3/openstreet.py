import xmltodict

fin = open('./files/map.osm', 'r', encoding='utf-8')

text = fin.read()
fin.close()
shops = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
     if 'tag' in node:
          tags = node['tag']
          if isinstance(tags, list):
               for tag in tags:
                    if '@k' in tag and tag['@k'] == 'shop':
                         shops += 1
print(shops)