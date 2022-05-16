mmod y x = mod x y

m3 = mmod 3
m5 = mmod 5


euler1 = sumMods [1..999]
    where accum x = m3 x == 0 || m5 x == 0
          sumMods xx = sum (filter accum xx)

notDivides a n = n `mod` a /= 0

sieve (x:xs) = x : (sieve (filter (notDivides x) xs))
primes = sieve [2..]

-- At this point the primes variable is lazy evaluated.
-- We can query this by using `take` to take n primes.
-- Instead, though, we'll want to use an aux function.

factors n = aux n primes
    where aux 1 _ = []
          aux n (p:ps) = case divMod n p of
                            (n', 0) -> p : aux n' ps
                            (_ , _) -> aux n ps

-- Here we're pattern matching using `divMod`. Note that
-- divMod n n = (1, 0) which would trigger the base case.

maxFactor n = foldr1 max $ factors n

euler3 = maxFactor 600851475143

-- problem 20

div10 a = a `div` 10
fact 0 = 1
fact n = n * fact (n - 1)
sumDigits 0 = 0
sumDigits n = n `mod` 10 + sumDigits (div10 n)
euler20 = sumDigits $ fact 100
