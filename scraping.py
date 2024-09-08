import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Fetch data from the URL
url = "https://www.whatmobile.com.pk/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Select phone names, prices, and images
names = soup.select("a.BiggerText")
prices = soup.select("span.PriceFont")
images = soup.select("img")

# Create and write to HTML file
file_path = r'C:\Users\Sher Ali\Desktop\scrap\index.html'  # Use raw string for file path
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Phone List</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Phone List</h1>
        <ul>
    ''')

    # Write data into the HTML file
    for name, price, image in zip(names, prices, images):
        # Handle relative URLs
        image_url = urljoin(url, image.get('src'))
        file.write(f'''
        <li>
            <img src="{image_url}" alt="{name.get_text(strip=True)}" style="width:200px;height:auto;">
            <h2>{name.get_text(strip=True)}</h2>
            <p>Price: {price.get_text(strip=True)}</p>
           
        </li>
        ''')

    file.write('''
        </ul>
    </body>
    </html>
    ''')

print("HTML file 'index.html' created successfully.")
