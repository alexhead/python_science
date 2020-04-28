from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read().decode('utf-8')
s = str(html)

soup = BeautifulSoup(s, 'lxml')
count = 0
for tag in soup.find_all("td"):
    count += int(tag.text)
print(count)





