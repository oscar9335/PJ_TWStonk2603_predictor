# Research
[Test and Trail.pdf](https://github.com/oscar9335/PJ_TWStonk2603_predictor/blob/576a9728cf50eacce213df8e4304a28d26a60090/%E5%80%8B%E4%BA%BA%E6%9C%9F%E6%9C%AB%E5%B0%88%E9%A1%8C_Final%20Report_F74076213_%E5%90%B3%E5%AE%9A%E6%B4%8B_%E9%95%B7%E6%A6%AE%E8%82%A1%E5%83%B9%E9%A0%90%E6%B8%AC.pdf)

## Data collection
### [crawallthe2603.py](https://github.com/oscar9335/PJ_TWStonk2603_predictor/blob/ea6065036b56eb1c8f8f3a5b6e51cd8b5b11f117/crawallthe2603%20.py) 
is used to crawl the stonk pricees of specific year from [台灣證券交易所](https://www.twse.com.tw/zh/index.html) and save the data as .csv, which use the

### [crawler_stockuse.py](https://github.com/oscar9335/PJ_TWStonk2603_predictor/blob/ea6065036b56eb1c8f8f3a5b6e51cd8b5b11f117/crawler_stockuse.py),
  * crawler_specfiv_stock(year,month,stock_number) <- function
    * the function take 3 input: the years you want, the month, and the stock_number, which is the stock symbol of a specifi company
  * crawler_Pow00(year,month) <- function
    * the years you want, the month, whick crawl the market trend price
  * pandas_convert(a_list) <- function
    * used to converst the list to pandas dataframe
 ## Data processing & model establish
 ### [.ipynb](https://github.com/oscar9335/PJ_TWStonk2603_predictor/blob/de83ef3dfa7b1adeed33617f183ffcf5e7aeb4f5/my2603predictor3.ipynb)
