from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import json
import os


data = load_iris()
X, y = data.data, data.target


model = RandomForestClassifier()
model.fit(X, y)


preds = model.predict(X)

acc = accuracy_score(y, preds)
os.makedirs("assets", exist_ok=True)


with open("assets/metrics.json", "w") as f:
    json.dump({"accuracy": acc}, f)

print("Accuracy:", acc)