
#include <iostream>
#include "model_inference.h"

int main() {
    float normal[7] = {5.0, 5.0, 0.0, 0.11, 0.21, 0.11, 0.21};
    float leak[7] = {5.0, 3.5, 1.5, 0.35, 0.60, 0.30, 0.55};
    float disturbance[7] = {5.0, 5.0, 0.0, 0.75, 1.20, 0.80, 1.30};

    std::cout << "NORMAL -> " << predictLeak(normal) << '\n';
    std::cout << "LEAK -> " << predictLeak(leak) << '\n';
    std::cout << "DISTURBANCE -> " << predictLeak(disturbance) << '\n';

    return 0;
}