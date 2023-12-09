from bs4 import BeautifulSoup
import requests
from ebooklib import epub

r = requests.get('https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-439/')
soup = BeautifulSoup(markup=r.content,features="lxml")
# chp_content = soup.find(id="content") -: is same as :- soup.find("div",{"id":"content"})
chp_content = soup.find("div",{"id":"content"})
unwanted_div = chp_content.find("div").extract() # this line extracts the unwanted div tag from the middle of the o/p and stores it in this var, so o/p doesnt displays it.
# chp = chp_content.find("p",recursive:=True)
# book = epub.EpubBook()


print(chp_content)