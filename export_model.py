
import joblib
from sklearn.tree import _tree

model = joblib.load("pipe_leak_model.pkl")
tree = model.tree_

FEATURES = [
    "inlet_flow",
    "outlet_flow",
    "flow_difference",
    "piezo1_rms",
    "piezo1_peak",
    "piezo2_rms",
    "piezo2_peak"
]

def generate_code(language):
    lines = []

    def walk(node, depth):
        indent = "    " * depth

        if tree.feature[node] != _tree.TREE_UNDEFINED:
            feature = FEATURES[tree.feature[node]]
            threshold = tree.threshold[node]

            lines.append(
                f"{indent}if (x[{tree.feature[node]}] <= {threshold:.8f}) {{"
            )
            walk(tree.children_left[node], depth + 1)
            lines.append(f"{indent}}} else {{")
            walk(tree.children_right[node], depth + 1)
            lines.append(f"{indent}}}")
        else:
            prediction = int(tree.value[node][0].argmax())
            lines.append(f"{indent}return {prediction};")

    walk(0, 1)

    if language == "cpp":
        return """// Generated Decision Tree
// Input order: inlet_flow, outlet_flow, flow_difference,
// piezo1_rms, piezo1_peak, piezo2_rms, piezo2_peak

int predictLeak(const float x[7]) {
""" + "\n".join(lines) + "\n}\n"

    return """// Generated Decision Tree
// Input order: inlet_flow, outlet_flow, flow_difference,
// piezo1_rms, piezo1_peak, piezo2_rms, piezo2_peak

function predictLeak(x) {
""" + "\n".join(lines) + "\n}\n"

with open("model_inference.h", "w") as f:
    f.write(generate_code("cpp"))

with open("model.js", "w") as f:
    f.write(generate_code("js"))

print("Export complete!")
print("Generated: model_inference.h")
print("Generated: model.js")
