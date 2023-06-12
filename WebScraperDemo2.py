from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "https://www.newegg.ca/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#prices = doc.find_all(string="$")
#parent = prices[0].parent
#strong = parent.find("strong")

price = doc.find("li", class_="price-current")
price = price.find("strong").string
print(price)


# Create a text file with the price
with open("price.txt", "w") as file:
    file.write(price)

# Get prices from text file and check if the new price is lower than the old price
with open("price.txt", "r") as file:
    old_price = file.read()
    print(old_price)

price = price.replace(",", "")  # Entfernt das Komma aus dem String
price = float(price)  # Konvertiert den String in eine Fließkommazahl

old_price = old_price.replace(",", "")
old_price = float(price)

if price < old_price:
    print("Price dropped!")
else:
    print("Price did not drop.")

