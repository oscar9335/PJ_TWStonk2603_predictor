import MySQLdb
import requests
from bs4 import BeautifulSoup

class Stock_history_value:
    def __init__(self, stock_number, year,month ):
        self.stock_number = stock_number
        self.year = year
        self.month = month
        # print(stock_number)
    
    def crawler(self):
        #if I use the wrong in this url it will redirect to the latest month
        response = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
            + self.year
            + self.month + "01" 
            + "&stockNo=" 
            + self.stock_number
            ,timeout=10)
        # print("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date="
        #     + self.year
        #     + self.month + "01" 
        #     + "&stockNo=" 
        #     + self.stock_number)

        soup = BeautifulSoup(response.text, "lxml")

        td = soup.find_all("td")

        all = tuple(item.text for item in td)
        # print(all)

        result = list()

        for i in range(0,len(all),9):
            a = (all[i],all[i+1],all[i+2],all[i+3],all[i+4],all[i+5],all[i+6],all[i+7],all[i+8])
            result.append(a)

        return result

stock_num = "3037"
year = "2021"
month = "12"

a = Stock_history_value(stock_num,year,month)
intodatabase = a.crawler()

conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = 'oscar9335',
                       db = 'mytestone',
                       charset='utf8')


cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS stockdata")

# sql = """CREATE TABLE stockdata(
#                 stocknumber VARCHAR(6),
#                 date VARCHAR(20),
#                 trading_volume_share VARCHAR(30),
#                 trading_price VARCHAR(15),
#                 opening  VARCHAR(10),
#                 higest  VARCHAR(10),
#                 lowest  VARCHAR(10),
#                 closing VARCHAR(10),
#                 dir VARCHAR(1),
#                 transaction VARCHAR(10),
#                 PRIMARY KEY (date))"""
# cur.execute(sql)
# conn.commit()

for entry in intodatabase[1:]:
    cur.execute("INSERT INTO stockdata(stocknumber,date, trading_volume_share, trading_price, opening,higest,lowest,closing,dir,transaction) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" 
        % (stock_num,entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7][0], entry[8]))
    conn.commit()

conn.close()