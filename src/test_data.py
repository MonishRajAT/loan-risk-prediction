import pandas as pd

# Loading the dataset
df = pd.read_csv("data/train.csv")

# Show first 5 rows 
print("First 5 rows of the dataset: ")
print(df.head())

print("\nDataset Shape: ")
print(df.shape)

print("\nColumn Names: ")
print(df.columns)