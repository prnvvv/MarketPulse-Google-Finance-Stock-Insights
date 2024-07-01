import requests
from bs4 import BeautifulSoup

NextPageURL = f"https://www.google.com/finance/quote/IDEA:NSE"
try:
    response = requests.get(NextPageURL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error while fetching data fro {NextPageURL}.")

soup2 = BeautifulSoup(response.text, "lxml")
   
ChangeValue = soup2.find_all("span", class_ = "P2Luy Ebnabc ZYVHBb")

print(ChangeValue)