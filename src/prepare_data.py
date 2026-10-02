import pandas as pd

# Load dataset
file_path = "dataset/phishing dataset csv.csv"

data = pd.read_csv(file_path)

print("Original dataset shape:")
print(data.shape)

# Remove index column
if "index" in data.columns:
    data = data.drop("index", axis=1)

# Separate features and target
X = data.drop("Result", axis=1)
y = data["Result"]

print("\nFeatures shape:")
print(X.shape)

print("\nTarget shape:")
print(y.shape)

print("\nTarget values:")
print(y.value_counts())

print("\nData preparation completed successfully!")