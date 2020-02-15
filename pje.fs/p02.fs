namespace Problems

module p02=
    let sum i j = i + j

    let rec fibonacciSum(i1:int,i2:int,max:int):int=
        if sum i1 i2 <= max then
            if sum i1 i2 % 2 = 0 then
                sum i1 i2 + fibonacciSum(i2,sum i1 i2, max)
            else fibonacciSum(i2,sum i1 i2,max)
        else 0

    let solve() : int=
        fibonacciSum(1,1,4000000)
