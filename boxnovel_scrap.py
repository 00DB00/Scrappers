from bs4 import BeautifulSoup
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

chps = []
chps.append("nav")
book = epub.EpubBook()
book.set_title('Abe_wiz')
description = epub.EpubHtml(title='Introduction',file_name='intro.xhtml',lang='en',content=u'<html><head></head><body><h1>Introduct</h1><p>Hola!!!</p></body></html>')
book.add_item(description)
chps.append(description)

def boxnovel_scrap(chp_link,i): 
    r = requests.get(f'{chp_link}')
    soup = BeautifulSoup(markup=r.content,features="lxml")
    chp_content = soup.find("div",{"text-left"})
    # unwanted_div = chp_content.find("div").extract() # this line extracts the unwanted div tag from the middle of the o/p and stores it in this var, so o/p doesnt displays it.
    chp_title = chp_content.find('h3').text.strip()
    paragraph = f"<p>{chp_title}</p>"
    content = chp_content.find_all("p")
    for j in content:
        con = j.text.strip()
        paragraph = paragraph + f"<p>{con}</p>"
    chapter = epub.EpubHtml(title=chp_title,file_name=f"chapter_{i+1}.xhtml",lang='en',content=paragraph)
    book.add_item(chapter)
    chps.append(chapter)

i = 0
while i < 2:
    ch = f"https://boxnovel.com/novel/abe-the-wizard-boxnovel/chapter-{i+1}/"
    boxnovel_scrap(ch,i)
    # f = open(f"D:\\PROJECTS\\Git_Projects\\Scrapers\\NewFolder\\chapter_{i+1}","x")
    # f.write(txt[i])
    i += 1

# Defining index of book 
book.toc = ( epub.Link(href='intro.xhtml',title='Introduction',uid='intro'), (epub.Section('Chapters'),(chps)) )
 
# Adding navigation files 
book.add_item(epub.EpubNcx()) 
book.add_item(epub.EpubNav()) 

book.spine = chps
epub.write_epub(f"D:\\PROJECTS\\Git_Projects\\Scrapers\\NewFolder\\test1.epub",book,{})
print(" xxxx -- complete -- xxxx ")
