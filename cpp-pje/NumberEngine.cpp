//
// Created by Miles Possing on 09-22.
//

#include "NumberEngine.h"
#include <cmath>

bool NumberEngine::IsPrime(int n) {
    int limit = ceil(sqrt(n));
    for (int i = 2; i < limit; i++){
        if (n % i == 0) return false;
    }
    return true;
}