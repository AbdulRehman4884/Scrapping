import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://myshop.pk/laptops-desktops-computers?cat=7"
data = {
    'title': [],
    'price': [],
    'specification': [],
    'image_link': []
}

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

products = soup.find_all('div', class_='product-item-info')

for product in products:
    title = product.find('a', class_='product-item-link').text.strip()
    price = product.find('span', class_='price').text.strip()
    specification_tag = product.find('div', class_='mso_listing_detail')
    specification = specification_tag.text.strip() 
    image_link = product.find('img', class_='product-image-photo')['src']

    data['title'].append(title)
    data['price'].append(price)
    data['specification'].append(specification)
    data['image_link'].append(image_link)

df = pd.DataFrame.from_dict(data)
df.to_csv("Laptop_data.csv",index=False)
