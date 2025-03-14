import requests
import json
from DBManager import DBManager
myDB =DBManager()
sql = """
    INSERT INTO tb_stocks(item_code, close_price)
    VALUES (:1, :2)"""
for page in range(1, 25):
    url = f"https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={page}&pageSize=100"
    res = requests.get(url)
    if res.status_code == 200:
        stocks = json.loads(res.text)['stocks']
        for stock in stocks:
            code = stock['itemCode']
            price = stock['closePrice'].replace(',', '')
            myDB.insert(sql,[code, price])

