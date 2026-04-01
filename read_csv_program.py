import pandas as pd

df = pd.read_csv("experience.csv")

print("Content of the file:")
print(df)

rows, columns = df.shape
print("\nRows:", rows)
print("Columns:", columns)

print("\nLength of dataframe:", len(df))

print("\nFirst 2 rows:")
print(df.head(2))
