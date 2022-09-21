import numpy as np
import pandas as pd

file = pd.read_csv("2603from201001to202206.csv")

print(file)


# # 將date轉換成日期類型
# d = file['1']
# for i in range(len(d)):
#     d.iloc[i]=d.iloc[i].replace(d.iloc[i][0:3], str(int(d.iloc[i][0:3]) + 1911))
# d.head()
# print('-'*20)
# d=pd.to_datetime(d,format='%Y/%m/%d')

# # 並將「日期」列設置為索引。
# file['date'] = pd.to_datetime(file['date']) 
# cluster_data = file.set_index(['date'], drop=True)

# cluster_data.to_csv("testchange.csv",index=False)

