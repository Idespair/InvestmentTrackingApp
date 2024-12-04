from Currency import query_currency
from Stock import query_stock

a = "usd"
b = "uah"

Currency_test = query_currency(a,b)
print(Currency_test)