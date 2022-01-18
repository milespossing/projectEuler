// module pje.fs.p04

//     open Utilities

//     let rec solve_rec(m:int64,n:int64):int64=
//         if NumberOperations.IntIsPalendrome(m*n) then
//             m * n
//         elif n = 100L then
//             solve_rec(m-1L,999L)
//         else
//             solve_rec(m,n-1L)
        
//     let solve:int64=
//         solve_rec(999L,999L)