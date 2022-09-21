import crawler_stockuse as craw

a = []


# for i in range(2011,2021,1):
    # enteryear = str(i)
enteryear = '2022'
for j in ['01','02','03','04','05','06']:
    a = craw.crawler_specfiv_stock(stock_number = "2603",year = enteryear,month = j)
    xx = craw.pandas_convert(a)
    filename = "2603"+ enteryear + j + ".csv"
    xx.to_csv(filename,index=False)
    print(filename + "finish")

# ['01','02','03','04','05','06']
# ['07','08','09','10','11','12']
# ['01','02','03','04','05','06','07','08','09','10','11','12']

# xx = craw.pandas_convert(a)
# print(xx)
# xx.to_csv("2603201002.csv",index=False)