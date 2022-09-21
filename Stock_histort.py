import requests
from bs4 import BeautifulSoup
import pandas as pd


class Stock_history_value:
    def __init__(self, stock_number, year,month ):
        self.stock_number = stock_number
        self.year = year
        self.month = month
        # print(stock_number)
    
    def crawler_specfiv_stock(self):
        #if I use the wrong in this url it will redirect to the latest month
        response = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
            + self.year
            + self.month + "01" 
            + "&stockNo=" 
            + self.stock_number
            ,timeout=10)
        print("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
            + self.year
            + self.month + "01" 
            + "&stockNo=" 
            + self.stock_number)

        soup = BeautifulSoup(response.text, "lxml")

        td = soup.find_all("td")

        all = tuple(item.text for item in td)
        # print(all)

        result = list()

        for i in range(0,len(all),9):
            a = (all[i],all[i+3],all[i+4],all[i+5],all[i+6],all[i+8],all[i+7])
            result.append(a)

        return result

    def crawler(self):
        #if I use the wrong in this url it will redirect to the latest month
        response = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
            + self.year
            + self.month + "01" 
            + "&stockNo=" 
            + self.stock_number
            ,timeout=10)
        print("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
            + self.year
            + self.month + "01" 
            + "&stockNo=" 
            + self.stock_number)

        soup = BeautifulSoup(response.text, "lxml")

        td = soup.find_all("td")

        all = tuple(item.text for item in td)
        # print(all)

        result = list()

        for i in range(0,len(all),9):
            a = (all[i],all[i+3],all[i+4],all[i+5],all[i+6],all[i+8],all[i+7])
            result.append(a)

        return result

    def pandas_convert(self,a_list):
        data = pd.DataFrame(a_list)
        # data.columns('日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數')
        return data



a = Stock_history_value("2063","2021","01")
aaaa = a.crawler_specfiv_stock()

# print(aaaa[1])

print(a.pandas_convert(aaaa))

# 大盤
# https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=html&date=20220530