import copy


def fillCell(cell,candidates):
    if len(candidates) == 1:
        cell.value = candidates[0]
        print(f"Filling {candidates[0]} at ({cell.row},{cell.col})")
        return True
    return False


def getCandidates(cell):
    candidates = list(range(1, 10))
    row = [i for i in cell.getRow() if i != 0]
    col = [i for i in cell.getColumn() if i != 0]
    bloc = [i for i in cell.getBlock() if i != 0]
    for i in row:
        if i in candidates: candidates.remove(i.value)
    for i in col:
        if i in candidates: candidates.remove(i.value)
    for i in bloc:
        if i in candidates: candidates.remove(i.value)
    return candidates

def solve(Game):
    goodRound = True
    while goodRound:
        goodRound = False
        for cell in Game:
            if (cell == 0):
                candidates = getCandidates(cell)
                if len(candidates) == 0:
                    print("BACK TRACK")
                    return None
                success = fillCell(cell,candidates)
                goodRound = success or goodRound
    if 0 in Game:
        Game = guess(Game)
    else:
        print('solved!')
    return Game

def guess(Game):
    candidates = 9
    for cell in Game:
        if cell != 0: continue
        currentCandidates = len(getCandidates(cell))
        if currentCandidates < candidates:
            easy = cell
            candidates = currentCandidates
    easyCandidates = getCandidates(easy)
    for c in easyCandidates:
        newGame = copy.deepcopy(Game)
        easyCopy = newGame.getCell(easy.row,easy.col)
        print(f"Trying {c} at ({easy.row},{easy.col})")
        easyCopy.value = c
        solution = solve(newGame)
        if solution is not None:
            return solution
