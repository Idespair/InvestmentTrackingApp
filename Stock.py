import requests
from bs4 import BeautifulSoup

#Function receives the name of a stock and searches for it on Google
def query_stock(stock):
    url = f'https://www.google.com/search?q=stock {stock}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    #If the research is successful the code starts looking inside the page's HTML content
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    #Tries to find the stock's price and currency through their classes and return price + currency
        try:
            stock = soup.find('span', {'class': 'IsqQVc NprOob wT3VGc'}).text
            currency = soup.find('span', {'class': 'knFDje'}).text
            return stock + currency
        except AttributeError:
            return "Error: Could not find stock price"
    
    else:
        return "Error: Could not retrieve data"
#User selects a stock and the value the function is called with said value attributed to it