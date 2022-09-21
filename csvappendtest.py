from pickle import FALSE
import numpy as np
import pandas as pd

the2603201001 = pd.read_csv("2603201001.csv")
thetotal = the2603201001

for i in range(2010,2023,1):
    year = str(i)
    if i == 2010:
        for j in ['02','03','04','05','06','07','08','09','10','11','12']:
            toappend = pd.read_csv("2603" + year + j + ".csv")
            thetotal = thetotal.append(toappend).reset_index(drop = True)

    elif i == 2022:
        for j in ['01','02','03','04','05','06']:
            toappend = pd.read_csv("2603" + year + j + ".csv")
            thetotal = thetotal.append(toappend).reset_index(drop = True)
    
    else:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            toappend = pd.read_csv("2603" + year + j + ".csv")
            thetotal = thetotal.append(toappend).reset_index(drop = True)

thetotal.to_csv("2603from201001to202206.csv",index=False)