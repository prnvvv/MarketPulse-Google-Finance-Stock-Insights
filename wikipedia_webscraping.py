import requests
from bs4 import BeautifulSoup

word = input("Enter the Word to search: ")
word = word.capitalize()

URL = f"https://en.wikipedia.org/wiki/{word}"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

SearchName = soup.find("a", class_ = "mw-selflink selflink").text

Definition = soup.find("blockqoute", class_ = "templatequote").text

print(Definition)

