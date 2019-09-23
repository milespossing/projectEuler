//
// Created by Miles Possing on 09-22.
//

#include "Problem.h"
#include "Solution.h"
#include <ctime>

 Solution Problem::Solve() {
    std::clock_t start;
    double duration;

    start = std::clock();
    int output = Algorithm();
    duration = (std::clock() - start) / (double) CLOCKS_PER_SEC;

}