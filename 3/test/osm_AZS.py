import xmltodict
import urllib.request

#destination = '../files/map_azs.osm'
#url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
#urllib.request.urlretrieve(url, destination)

fin = open('../files/map_azs.osm', 'r', encoding='utf-8')

text = fin.read()
fin.close()

dct = xmltodict.parse(text)
azs = 0
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list):
            for tag in tags:
                if '@v' in tag and tag['@v']=='fuel':
                    flag = True
                    azs += 1
        elif isinstance(tags, dict): #заправка которая находится не в словаре
            if (tags['@v']) == 'fuel':
                azs +=1
                #if '@k' in tag and tag['@k']=='name' and flag == True:
                    #print(tag['@v']) # названия АЗС
for way in dct['osm']['way']:
    if 'tag' in way:
        tags = way['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list):
            for tag in tags:
                if '@v' in tag and tag['@v']=='fuel':
                    flag = True
                    azs += 1
        elif isinstance(tags, dict): #заправка которая находится не в словаре
            if (tags['@v']) == 'fuel':
                azs +=1
print(azs)