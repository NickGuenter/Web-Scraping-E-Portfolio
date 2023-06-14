# Importing the required libraries
import requests
from bs4 import BeautifulSoup

# URL for scrapping data
url = "http://quotes.toscrape.com/"

# Sending request to the website and getting the response back
request = requests.get(url)

# Parse HTML code for the entire site using Beautiful Soup
soup = BeautifulSoup(request.text, "html.parser")

# Get all quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Print out the quotes and corresponding authors
for i in range(len(quotes)):
    print(quotes[i].text)
    print("Author: " + authors[i].text)
    print()

# For other solution:
# If you like, you can also create a list for quotes and a list for authors
# and zip them together (Hint: use zip() function) to get a list of tuples and print them out
quotes_list = []
authors_list = []
# Append the quotes and authors to the lists
for i in range(len(quotes)):
    quotes_list.append(quotes[i].text)
    authors_list.append(authors[i].text)

# Zip the two lists together and print them out
for t in zip(quotes_list, authors_list):
    print(t)



