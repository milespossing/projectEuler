#include <iostream>
#include "problems/Problem.h"
#include "problems/Solution.h"

int main() {
    Problem p = new Problem1();
    Solution s = p.Solve();
    std::cout << "Hello, World!" << std::endl;

}