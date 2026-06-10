import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("crime_dataset.csv")

X = df[['Population', 'Unemployment', 'PovertyRate']]
y = df['Crime']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("="*40)
print("Crime Prediction Model")
print("="*40)
print(f"Accuracy: {accuracy*100:.2f}%")

# Save Model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")