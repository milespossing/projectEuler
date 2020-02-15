namespace Problems

module p01=
    let rec recurse (i:int) : int=
        if (i = 3) then
            3
        else
            if (i % 3 = 0 || i % 5 = 0) then
                i + recurse (i - 1)
            else recurse (i - 1)

    let solve() : int=
        recurse 999
