# Problem 86

## Problem

This problem centers around cuboids and the shortest routes from one vertex to the opposite. 
The question is if _m_ is the maximum side length of the cuboid, what is the minimum _m_ for which the number of distinct cuboids have *integer* solutions for the shortest path from one corner to the other.

I've worked out that the shortest route will always be the square root of the product of the largest number and the sum of the two smaller numbers. 
This means that if the product of the largest number and the sum of the two smallest numbers is a square number, the solution will be an integer.

I also know that for each _m_, the number of solutions is necessarily the sum of the number of solutions for _m-1_ and the number of solutions where the side length of one of the edges of the cuboid is _m_. Finally, I know that the product of two numbers will be square if for each of their prime factors, the modulus(2) of the exponent of each prime factor is equal. If I kept a dictonary of integers less than m containing an array of prime factor counts and used such an array to test for squaring pairs, I could find if numbers would be square quite quickly. This would still leave a runtime of m^2 for each m with a neglegible runtime for the prime pairing and prime factorization of m.
