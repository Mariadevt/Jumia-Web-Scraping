# -*- coding: utf-8 -*-
"""Jumia Web Scraping

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gPFWQlC_glJKRDLrS73aeqwOkwmHkhng
"""

#Objective - Extract liquor names and prices from the beer, wine and spirits category

#import necessary libraries used for web scraping

!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
import re

#Url of the page to scrape

url = "https://www.jumia.co.ke/beer-wine-spirits/"

#Send a GET request to the URL

response = requests.get(url)

#Parse the HTML contents

soup = BeautifulSoup(response.content, "html.parser")

#Find all the products on the page

products_names = soup.find_all("div", class_= "name")
prices = soup.find_all("div", class_="prc")

cleaned_product_names = []
cleaned_prices = []

# Clean the extracted data by removing unwanted characters or formatting
for name in product_names:
    cleaned_name = re.sub(r"\s+", " ", name.text.strip())
    cleaned_product_names.append(cleaned_name)

for price in prices:
    cleaned_price = re.sub(r"[^\d.]", "", price.text.strip())
    cleaned_prices.append(cleaned_price)

# Compile data into a list of dictionaries
data_list = []
for i in range(len(cleaned_product_names)):
    data_list.append({
        "Product Name": cleaned_product_names[i],
        "Price": cleaned_prices[i]
    })

# Print the cleaned data
for i in range(len(cleaned_product_names)):
    print("Product Name:", cleaned_product_names[i])
    print("Price:", cleaned_prices[i])
    print("")

# Write data to CSV file
csv_filename = "jumia.csv"
csv_columns = ["Product Name", "Price"]

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print(f"Data written to {csv_filename}")

from google.colab import files
files.download('jumia.csv')

