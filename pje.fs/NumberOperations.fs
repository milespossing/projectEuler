namespace Utilities

open System

module NumberOperations=
    let rec ConvertToDigitArrayRec(n:int64,p:int)=
            if n = 0L then [] else
            let dig = n / int64(Math.Pow(float(10),float(p)))
            let v = dig * int64(Math.Pow(float(10),float(p)))
            dig :: ConvertToDigitArrayRec(n - v,p - 1)
            
    let ConvertToDigitArray(n:int64)=
        let l = int(floor(Math.Log10(float(n))))
        ConvertToDigitArrayRec(n,l)
      
    // let IntIsPalendrome(n:int64):bool=
    //     let l = ConvertToDigitArray(n)
    //     let a1 = l.[0..(l.Length / 2) - 1]
    //     let a2 = l.[(l.Length/2)..] |> List.rev
        
        