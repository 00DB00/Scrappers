from bs4 import BeautifulSoup
import requests

r = requests.get('https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-439/')
soup = BeautifulSoup(markup=r.content,features="lxml")
chp_content = soup.find(id="content").extract(div)
print(chp_content)

