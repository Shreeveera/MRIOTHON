// Generated Random Forest - 5 Decision Trees

const forest = [
function(x) {
    if (x[6] <= 0.93500000) {
        if (x[2] <= 0.69999998) {
            return 0;
        } else {
            return 1;
        }
    } else {
        return 2;
    }
},
function(x) {
    if (x[1] <= 4.29999995) {
        return 1;
    } else {
        if (x[6] <= 0.74499998) {
            return 0;
        } else {
            return 2;
        }
    }
},
function(x) {
    if (x[2] <= 0.64999998) {
        if (x[4] <= 0.68999999) {
            return 0;
        } else {
            return 2;
        }
    } else {
        return 1;
    }
},
function(x) {
    if (x[6] <= 0.38500001) {
        return 0;
    } else {
        if (x[3] <= 0.53999999) {
            return 1;
        } else {
            return 2;
        }
    }
},
function(x) {
    if (x[1] <= 4.29999995) {
        return 1;
    } else {
        if (x[2] <= 0.05000000) {
            return 2;
        } else {
            if (x[1] <= 5.04999995) {
                return 2;
            } else {
                return 0;
            }
        }
    }
}
];


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
