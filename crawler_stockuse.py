import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawler_specfiv_stock(year,month,stock_number):
    #if I use the wrong in this url it will redirect to the latest month
    print("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
        + year
        + month + "01" 
        + "&stockNo=" 
        + stock_number)
        
    response = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
        + year
        + month + "01" 
        + "&stockNo=" 
        + stock_number
        ,timeout=100)
    

    soup = BeautifulSoup(response.text, "lxml")

    td = soup.find_all("td")

    all = tuple(item.text for item in td)
    # print(all)

    result = list()

    for i in range(9,len(all),9):
        a = (all[i],all[i+3],all[i+4],all[i+5],all[i+6],all[i+8],all[i+7])
        result.append(a)

    return result

def crawler_Pow00(year,month):
        #if I use the wrong in this url it will redirect to the latest month
    response = requests.get("https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=html&date="
        + year
        + month + "01" 
        ,timeout=100)

    soup = BeautifulSoup(response.text, "lxml")

    td = soup.find_all("td")

    all = tuple(item.text for item in td)
    # print(all)

    result = list()

    for i in range(0,len(all),5):
        a = (all[i],all[i+1],all[i+2],all[i+3],all[i+4])
        result.append(a)

    return result

def pandas_convert(a_list):
    data = pd.DataFrame(a_list)
    # data.columns('日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數')
    return data