import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/markets/losers"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error while fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

CompanyNames = soup.find_all("div", class_ = "ZvmM7")

for name in CompanyNames:
    print(name.text)


