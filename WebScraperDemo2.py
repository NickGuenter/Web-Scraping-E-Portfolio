# Importing the libraries requests and BeautifulSoup
from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "https://www.newegg.ca/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771"

# Sending request to the website and getting the response back
# Parse HTML code for the entire site using Beautiful Soup
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# Alternative way to get the HTML from the website
    #prices = doc.find_all(string="$")
    #parent = prices[0].parent
    #strong = parent.find("strong")

# Get the price from the website
price = doc.find("li", class_="price-current")
price = price.find("strong").string

priceString = price
print("New Price: " + price)

# Get prices from text file and check if the new price is lower than the old price
with open("price.txt", "r") as file:
    old_price = file.read()
    print("Old Price: " + old_price)

# Convert the prices to floats
price = price.replace(",", "")
price = float(price)
old_price = old_price.replace(",", "")
old_price = float(old_price)

# Check if the price dropped
if price < old_price:
    print("Price dropped!")
if price > old_price:
    print("Price increased!")
else:
    print("Price did not drop.")

# Write the new price to the text file
with open("price.txt", "w") as file:
    file.write(priceString)
    file.close()