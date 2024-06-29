import requests
from bs4 import BeautifulSoup

word = input("Enter the Word to search: ")
word = word.capitalize()

URL = f"https://en.wikipedia.org/wiki/{word}"

response = requests.get(URL)
response.text