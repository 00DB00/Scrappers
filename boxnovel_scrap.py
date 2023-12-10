import string
from bs4 import BeautifulSoup, Tag
import requests
from ebooklib import epub

# r = requests.get('https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-439/')
# soup = BeautifulSoup(markup=r.content,features="lxml")
# # chp_content = soup.find(id="content") -: is same as :- soup.find("div",{"id":"content"})
# chp_content = soup.find("div",{"id":"content"})
# unwanted_div = chp_content.find("div").extract() # this line extracts the unwanted div tag from the middle of the o/p and stores it in this var, so o/p doesnt displays it.
# # chp = chp_content.find("p",recursive:=True)
# # book = epub.EpubBook()
# # new_tag_p = soup.new_tag("p")
# # new_tag_p.string = chp_content.get_text(strip=True)
# # chp_content.replace_with(new_tag_p)
# txt = [chp_content.text]
# print(txt)

txt = []
title = []
chp = []
book = epub.EpubBook()
book.set_title('Abe_wiz')

def boxnovel_scrap(chp_link): 
    r = requests.get(f'{chp_link}')
    # print(r)
    soup = BeautifulSoup(markup=r.content,features="lxml")
    chp_content = soup.find("div",{"text-left"})
    # unwanted_div = chp_content.find("div").extract() # this line extracts the unwanted div tag from the middle of the o/p and stores it in this var, so o/p doesnt displays it.
    # print(chp_content)
    chp_title = chp_content.find('h3').text
    title.append(chp_title)
    # print(chp_title)
    txt.append(chp_content)


i = 0
while i < 1:
    ch = f"https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-{i+1}/"
    # print(ch)
    boxnovel_scrap(ch)
    # f = open(f"D:\\PROJECTS\\Git_Projects\\Scrapers\\NewFolder\\chapter_{i+1}","x")
    # f.write(txt[i])
    chapter = epub.EpubHtml(title=title[i],file_name=f"chapter_{i+1}.xhtml",lang='en',content=txt[i])
    book.add_item(chapter)
    chp.append(chapter)
    i += 1

epub.write_epub(f"D:\\PROJECTS\\Git_Projects\\Scrapers\\NewFolder\\test1.epub",book,{})
print("complete")
# print(txt)
