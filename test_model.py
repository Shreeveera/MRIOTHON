
import joblib
import pandas as pd

model = joblib.load("pipe_leak_model.pkl")

tests = {
    "NORMAL": [5.0, 5.0, 0.0, 0.11, 0.21, 0.11, 0.21],
    "LEAK": [5.0, 3.5, 1.5, 0.35, 0.60, 0.30, 0.55],
    "DISTURBANCE": [5.0, 5.0, 0.0, 0.75, 1.20, 0.80, 1.30]
}

labels = {
    0: "NORMAL",
    1: "LEAK",
    2: "DISTURBANCE"
}

features = [
    "inlet_flow", "outlet_flow", "flow_difference",
    "piezo1_rms", "piezo1_peak", "piezo2_rms", "piezo2_peak"
]

for name, values in tests.items():
    input_data = pd.DataFrame([values], columns=features)
    prediction = model.predict(input_data)[0]
    print(f"{name} input -> {labels[prediction]}")
