import pandas as pd
student_total={"s1":230,"s2":235,"s3":450,"s4":500}
series=pd.Series(student_total)
print(series["s2"])