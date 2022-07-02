import requests
import csv

symbols = ['AAPL','AMZN','NFLX','GOOGL']
header = ['stock_symbol','percentage_change','current_price','last_close_price']

most_volatile_stock = {
  'stock_symbol': '',
  'percentage_change':0,
  'current_price':0,
  'last_close_price':0
}

for symbol in symbols: 
  r = requests.get('https://finnhub.io/api/v1/quote?symbol='+symbol+'&token=cb09fcaad3i37ovb0bfg')
  
  res = r.json()
  print(res)
  if(res['dp'] > most_volatile_stock['percentage_change']):
    most_volatile_stock['stock_symbol'] = symbol
    most_volatile_stock['percentage_change'] = res['dp']
    most_volatile_stock['current_price'] = res['c']
    most_volatile_stock['last_close_price'] = res['pc']

with open('most_volatile_stock.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    data = [most_volatile_stock['stock_symbol'],most_volatile_stock['percentage_change'],most_volatile_stock['current_price'],most_volatile_stock['last_close_price']]
    writer.writerow(data)