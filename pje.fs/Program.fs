// Learn more about F# at http://fsharp.org

namespace pje

open System
open Utilities
open pje.fs

module program=
    [<EntryPoint>]
    let main argv =
        let a = p04.solve
        printfn "%i" a
        0 // return an integer exit code
