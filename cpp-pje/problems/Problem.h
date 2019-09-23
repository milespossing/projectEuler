//
// Created by Miles Possing on 09-22.
//

#ifndef CPP_PJE_PROBLEM_H
#define CPP_PJE_PROBLEM_H

#include "Solution.h"

class Problem {
public:
    Solution Solve();

protected:
    virtual int Algorithm()=0;
};

#endif //CPP_PJE_PROBLEM_H
