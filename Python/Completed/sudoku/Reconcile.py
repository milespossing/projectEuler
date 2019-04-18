

def reconcile(game1,game2):
    for i in range(len(game1)):
        if game1.cells[i] != game2.cells[i] and game1.cells[i] != 0 and game2.cells[i] != 0:
            return False
    return True

def solved(game):
    for i in range(3):
        for j in range(3):
            row = game.getRow(3 * i + j)
            col = game.getColumn(3 * i + j)
            blk = game.getBlock(i,j)
            for k in range(9):
                if len(set(row)) != 9:
                    return False
                if len(set(col)) != 9:
                    return False
                if len(set(blk)) != 9:
                    return False
    return True