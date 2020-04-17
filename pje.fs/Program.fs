// Learn more about F# at http://fsharp.org

namespace pje

open System

module program=
    [<EntryPoint>]
    let main argv =
        let a = Problems.p03.solve(600851475143L)
        printfn "%i" a
        0 // return an integer exit code
