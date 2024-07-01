import requests
from bs4 import BeautifulSoup

NextPageURL = f"https://www.google.com/finance/quote/YESBANK:NSE"
try:
    response = requests.get(NextPageURL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error while fetching data fro {NextPageURL}.")

soup2 = BeautifulSoup(response.text, "lxml")
   
heading = soup2.find_all ("span", class_ = "P2Luy Ez2Ioe ZYVHBb")

print(heading)