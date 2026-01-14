import pandas as pd
employee={"e1":22000,"e2":23000,"e3":34000,"e4":43000}
series=pd.Series(employee)
print(series)
print("total",series.sum())
print(series.max())
print(series.min())
print(series.mean())
