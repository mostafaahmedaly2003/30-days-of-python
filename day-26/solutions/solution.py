# Day 26 - Web Scraping with BeautifulSoup | SOLUTION
# Try to solve exercises.py yourself before looking here!

import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')
for book in books[:5]:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f'{title}: {price}')
