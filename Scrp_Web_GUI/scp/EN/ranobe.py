import bs4 as bs
import requests 

# Getting Page response
usr_agent_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
page_response = requests.get(url='https://ranobes.top/',headers=usr_agent_header)

print(page_response)
