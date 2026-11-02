
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
import joblib

# PLACEHOLDER TRAINING DATA
# Replace these values with actual sensor readings later.

data = {
    "inlet_flow": [
        5.0, 5.1, 4.9, 5.2, 5.0,   # Normal
        5.0, 5.1, 4.9, 5.0, 5.2,   # Leak
        5.0, 5.1, 4.9, 5.2, 5.0    # Disturbance
    ],
    "outlet_flow": [
        5.0, 5.0, 4.9, 5.1, 5.0,
        3.5, 3.4, 3.6, 3.3, 3.5,
        5.0, 5.1, 4.9, 5.0, 5.1
    ],
    "flow_difference": [
        0.0, 0.1, 0.0, 0.1, 0.0,
        1.5, 1.7, 1.3, 1.7, 1.7,
        0.0, 0.0, 0.0, 0.2, -0.1
    ],
    "piezo1_rms": [
        0.10, 0.12, 0.11, 0.10, 0.13,
        0.35, 0.38, 0.32, 0.40, 0.36,
        0.75, 0.80, 0.70, 0.85, 0.78
    ],
    "piezo1_peak": [
        0.20, 0.22, 0.21, 0.20, 0.23,
        0.60, 0.65, 0.58, 0.70, 0.63,
        1.20, 1.30, 1.15, 1.40, 1.25
    ],
    "piezo2_rms": [
        0.11, 0.10, 0.12, 0.11, 0.10,
        0.30, 0.34, 0.32, 0.36, 0.31,
        0.80, 0.75, 0.85, 0.78, 0.82
    ],
    "piezo2_peak": [
        0.21, 0.20, 0.22, 0.21, 0.20,
        0.55, 0.60, 0.58, 0.62, 0.57,
        1.30, 1.25, 1.40, 1.35, 1.28
    ],
    "label": [
        0, 0, 0, 0, 0,       # NORMAL
        1, 1, 1, 1, 1,       # LEAK
        2, 2, 2, 2, 2        # DISTURBANCE
    ]
}

df = pd.DataFrame(data)

FEATURES = [
    "inlet_flow",
    "outlet_flow",
    "flow_difference",
    "piezo1_rms",
    "piezo1_peak",
    "piezo2_rms",
    "piezo2_peak"
]

X = df[FEATURES]
y = df["label"]

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

joblib.dump(model, "pipe_leak_model.pkl")

print("Model trained successfully!")
print("\nDecision Tree:")
print(export_text(model, feature_names=FEATURES))

print("\nClass mapping:")
print("0 = NORMAL")
print("1 = LEAK")
print("2 = DISTURBANCE")

print("\nModel saved as pipe_leak_model.pkl")
