// Generated Decision Tree
// Input order: inlet_flow, outlet_flow, flow_difference,
// piezo1_rms, piezo1_peak, piezo2_rms, piezo2_peak

int predictLeak(const float x[7]) {
    if (x[6] <= 0.38500001) {
        return 0;
    } else {
        if (x[5] <= 0.55500001) {
            return 1;
        } else {
            return 2;
        }
    }
}
