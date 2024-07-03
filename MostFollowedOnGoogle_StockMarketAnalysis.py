import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL} : {e}")

soup = BeautifulSoup(response.text, "lxml")

MFGCompanyNames = soup.find_all("div", class_ = "TwnKPb")

MFGCompanyNames_List = []

for name in MFGCompanyNames:
    MFGCompanyNames_List.append(name.text)

print(MFGCompanyNames_List)