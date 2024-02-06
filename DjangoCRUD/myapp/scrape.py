import requests
from bs4 import BeautifulSoup

url = 'https://www.laptop.lk/index.php/product-category/laptops/'  # Replace with the target website URL
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
