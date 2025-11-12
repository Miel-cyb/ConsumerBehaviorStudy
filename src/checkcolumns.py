import pandas as pd

file_path = "data/Consumer Purchase & Stock Prediction Study (Responses).xlsx"

data = pd.read_excel(file_path)

print("\n=== COLUMN HEADERS IN DATASET ===")
for i, col in enumerate(data.columns, start=1):
    print(f"{i}. {col}")
