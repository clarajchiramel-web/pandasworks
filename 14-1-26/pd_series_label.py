import pandas as pd
salary=[34000,35000,36000,37000]
series=pd.Series(salary,index=["e1","e2","e3","e4"])
print(series)
print(series["e1"])#34000
print(series["e3"])#35000
print(series["e1":"e3"])#1  35000
                  #2  36000
