    from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)

soup = BeautifulSoup(s, 'html.parser')
print(soup.find_all('a', href=True))