import pandas as pd

students={
    "name":["clara","sree","arya","angel"],
    "age":[23,24,23,21],
    "course":["ds","ds","dj","ds"]
}
df=pd.DataFrame(students)
print(df)
print(df[2:3]) #2 arya 23 dj
print(df["age"])
print(df[["age","course"]])
