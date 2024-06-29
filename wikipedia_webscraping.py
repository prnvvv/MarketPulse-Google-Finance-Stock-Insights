import requests
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/markets/gainers"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

CompanyNames = soup.find_all("div", class_ = "ZvmM7")

for name in CompanyNames:
    print(name.text)




