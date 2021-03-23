import requests
from bs4 import BeautifulSoup
import lxml


source = requests.get('https://devopscube.com/project-managment-software').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

article = soup.find('article')
headline = article.div.h3.text
print(headline)

officialWebsite = article.find('div', class_='entry-content').a.text
print(officialWebsite)