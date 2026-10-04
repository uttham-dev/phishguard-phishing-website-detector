import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# 1. Load dataset
file_path = "dataset/phishing dataset csv.csv"
data = pd.read_csv(file_path)

# 2. Remove index column
if "index" in data.columns:
    data = data.drop("index", axis=1)

# 3. Separate features and target
X = data.drop("Result", axis=1)
y = data["Result"]

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data split completed.")

# 5. Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 6. Train model
print("\nTraining model...")
model.fit(X_train, y_train)

print("Model training completed!")

# 7. Make predictions
y_pred = model.predict(X_test)

# 8. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

# 9. Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 10. Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# 11. Save trained model
joblib.dump(model, "model/phishing_model.pkl")

print("\nModel saved successfully!")
print("Location: model/phishing_model.pkl")