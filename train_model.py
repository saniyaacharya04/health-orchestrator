# train_model.py
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np

print("🚀 Training started...")

# Dummy training data: [CPU%, Memory%, Error rate]
X = np.array([
    [30, 40, 0.01],
    [90, 85, 0.3],
    [70, 75, 0.25],
    [40, 45, 0.02],
    [95, 95, 0.5],
])

# Labels: 0 = NO_ACTION, 1 = RESTART
y = [0, 1, 1, 0, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
