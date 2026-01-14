import pandas as pd
data=[55,50,66,65,67,69,70,76,72,53]
weight=pd.Series(data)
print(weight)
print(weight.head())#head
print(weight.tail())#tail
print(weight.shape)