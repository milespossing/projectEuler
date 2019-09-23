//
// Created by Miles Possing on 09-22.
//

#include "Problem.h"

class Problem1 : Problem
{
    int Algorithm() override {
        int output = 0;
        for (int i = 0; i < 1000; i++){
            if (i % 3 == 0 || i % 5 == 0){
                output += i;
            }
        }
        return output;
    }
};