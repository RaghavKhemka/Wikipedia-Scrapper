import requests
import re
from bs4 import BeautifulSoup
SearchTerm = str(input('Enter your Search term : '))
url ='https://en.wikipedia.org/wiki/Special:Search?search='+SearchTerm
response = requests.get(url)
page_source = response.text
soup = BeautifulSoup(page_source, 'html.parser')
for content in soup.find_all('p',limit = 8):
    line = content.get_text()
    type(line)
    line = re.sub('\[[0-9]+\]','',line)
    line = line.replace('(listen)','')
    print(line)
x = str(input("\n\nDo you want the full page? (Y/N) : "))
if x == 'Y' or x=='y':
    for content in soup.find_all('p', limit=None):
        line = content.get_text()
        type(line)
        line = re.sub('\[[0-9]+\]', '', line)
        line = line.replace('(listen)', '')
        print(line)




