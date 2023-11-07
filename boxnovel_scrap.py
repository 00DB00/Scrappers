from bs4 import BeautifulSoup
import requests

r = requests.get('https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-439/')
soup = BeautifulSoup(markup=r.content,features="lxml")
# chp_content = soup.find(id="content") -: is same as :- soup.find("div",{"id":"content"})
chp_content = soup.find("div",{"id":"content"})
#chp = chp_content.find("p",recursive:=True)
print(chp_content)