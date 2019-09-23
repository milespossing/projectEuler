cmake_minimum_required(VERSION 3.14)
project(cpp_pje)

set(CMAKE_CXX_STANDARD 14)

add_executable(cpp_pje main.cpp NumberEngine.cpp NumberEngine.h problems/Problem.cpp problems/Problem.h problems/Problem1.cpp problems/Solution.cpp problems/Solution.h)