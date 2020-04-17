namespace Problems

module p03=
    let rec recurse(i:int64,m:int64,t:int64):int64=
        if float(i) > sqrt(float(t)) then m else
        if t % i = 0L then
            if Utilities.NumberTheory.IsPrime(t / i) then
                t / i
            elif Utilities.NumberTheory.IsPrime(i) then
                recurse(i + 1L,i,t)
            else recurse(i + 1L,m,t)
        else recurse(i + 1L,m,t)

    let solve(n:int64) : int64=
        recurse(2L,0L,n)