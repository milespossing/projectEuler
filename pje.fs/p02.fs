namespace Problems

module p02=
    let rec fibonacciSum(i1:int,i2:int,max:int):int=
        if i1 + i2 <= max then
            if i1 + i2 % 2 = 0 then
                i1 + i2 + fibonacciSum(i2,i1 + i2, max)
            else fibonacciSum(i2,i1 + i2,max)
        else 0

    let solve() : int=
        fibonacciSum(1,1,4000000)
