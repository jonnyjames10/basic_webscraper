from bs4 import BeautifulSoup
import requests

query = 'bristol'
url = f'https://www.google.com/search?q=weather+{query}'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html', features='lxml')

soup.find(string = '18')
print(soup)
