import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
URL = 'https://www.meesho.com/robots.txt'  # Replace with the actual URL
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract product details
products = []
for item in soup.find_all('div', class_='product-item'):
    name = item.find('h2', class_='product-name').text
    price = item.find('span', class_='price').text
    rating = item.find('div', class_='rating').text
    products.append([name, price, rating])

# Step 4: Store the data in a CSV file
df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Rating'])
df.to_csv('products.csv', index=False)

print("Data has been scraped and saved to products.csv")
