
const { predictLeak } = require("./model.js");

const tests = {
    NORMAL: [5.0, 5.0, 0.0, 0.11, 0.21, 0.11, 0.21],
    LEAK: [5.0, 3.5, 1.5, 0.35, 0.60, 0.30, 0.55],
    DISTURBANCE: [5.0, 5.0, 0.0, 0.75, 1.20, 0.80, 1.30]
};

const labels = ["NORMAL", "LEAK", "DISTURBANCE"];

for (const [name, values] of Object.entries(tests)) {
    const prediction = predictLeak(values);
    console.log(`${name} input -> ${labels[prediction]}`);
}
module.exports = { predictLeak };