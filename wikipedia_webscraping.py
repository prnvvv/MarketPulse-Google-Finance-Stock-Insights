import requests
from bs4 import BeautifulSoup

URL = f"https://www.moneycontrol.com/stocksmarketsindia/"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

MostActiveStocks = soup.find("div", class_ = "title14_mh brd_bot").text

tables = soup.find("table", class_ = "mctable1")

name = tables.find("td", class_ = "tdred").find("a", class_ = "robo_medium").text

print(name)




