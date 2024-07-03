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