
notDivides a n = n `mod` a /= 0
sieve (x:xs) = x : sieve (filter (notDivides x) xs)
primes = sieve [2..]