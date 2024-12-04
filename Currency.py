import requests
from bs4 import BeautifulSoup

def query_currency(currencyOrigin, currencyDestiny):
    url = f'https://www.google.com/search?q= {currencyOrigin} to {currencyDestiny}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            currency = soup.find('span', {'class': 'DFlfde SwHCTb'}).text
            return currency
        except AttributeError:
            return "Error: Could not find stock price"
    
    else:
        return "Error: Could not retrieve data"

#This function takes two values, a currency that should be converted to another one