namespace Utilities

module NumberTheory=
    let rec IsPrimeRec(n:int64,i:int64)=
        if (float(i) > sqrt(float(n))) then
            true
        else
        if (n % i = 0L) then
            false
        else
            IsPrimeRec(n,i+1L)

    let IsPrime(n)=
        IsPrimeRec(n,2L)

        