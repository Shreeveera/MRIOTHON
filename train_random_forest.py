
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import _tree

# Same placeholder dataset used for Decision Tree
data = {
    "inlet_flow": [
        5.0, 5.1, 4.9, 5.2, 5.0,
        5.0, 5.1, 4.9, 5.0, 5.2,
        5.0, 5.1, 4.9, 5.2, 5.0
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
    "label": [0]*5 + [1]*5 + [2]*5
}

FEATURES = [
    "inlet_flow", "outlet_flow", "flow_difference",
    "piezo1_rms", "piezo1_peak", "piezo2_rms", "piezo2_peak"
]

df = pd.DataFrame(data)

X = df[FEATURES]
y = df["label"]

model = RandomForestClassifier(
    n_estimators=5,
    max_depth=4,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "random_forest_model.pkl")

# Export all trees into JavaScript
def export_tree(tree):
    t = tree.tree_
    lines = []

    def walk(node, depth):
        indent = "    " * depth

        if t.feature[node] != _tree.TREE_UNDEFINED:
            feature = t.feature[node]
            threshold = t.threshold[node]

            lines.append(
                f"{indent}if (x[{feature}] <= {threshold:.8f}) {{"
            )
            walk(t.children_left[node], depth + 1)
            lines.append(f"{indent}}} else {{")
            walk(t.children_right[node], depth + 1)
            lines.append(f"{indent}}}")
        else:
            prediction = int(t.value[node][0].argmax())
            lines.append(f"{indent}return {prediction};")

    walk(0, 1)

    return "function(x) {\n" + "\n".join(lines) + "\n}"

tree_functions = [
    export_tree(estimator)
    for estimator in model.estimators_
]

js = "// Generated Random Forest - 5 Decision Trees\n\n"
js += "const forest = [\n"
js += ",\n".join(tree_functions)
js += "\n];\n\n"

js += """
function predictRandomForest(x) {
    const votes = [0, 0, 0];

    for (const tree of forest) {
        votes[tree(x)]++;
    }

    return votes.indexOf(Math.max(...votes));
}

if (typeof module !== "undefined") {
    module.exports = { predictRandomForest };
}
"""

with open("model_rf.js", "w") as f:
    f.write(js)

print("Random Forest trained successfully!")
print("Trees:", len(model.estimators_))
print("Saved: random_forest_model.pkl")
print("Exported: model_rf.js")
