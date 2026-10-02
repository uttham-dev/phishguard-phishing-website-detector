import pandas as pd

# Load the dataset
file_path = "dataset/phishing dataset csv.csv"

data = pd.read_csv(file_path)

# Display basic information
print("Dataset loaded successfully!")
print("Shape:", data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nFirst 5 rows:")
print(data.head())