// Learn more about F# at http://fsharp.org

namespace pje

open System

module program=
    [<EntryPoint>]
    let main argv =
        let a = Problems.p01.solve()
        printfn "%i" a
        0 // return an integer exit code
