square :: Int -> Int
square n = n * n
p6 :: Int -> Int
p6 n = (square (foldr (+) 0 [1..n])) - (foldr ((+) . square) 0 [1..n])