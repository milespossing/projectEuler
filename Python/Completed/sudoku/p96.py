from Timer import timer
from Game import Game
import Solver
from Reconcile import reconcile, solved
import copy

def getGames(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    current = []
    output = []
    while len(lines) > 0:
        if lines[0][0] == 'G':
            if (len(current) > 0): output.append(current)
            current = []
            lines.pop(0)
        else:
            current.append(lines.pop(0))
    output.append(current)
    return output


@timer
def solve():
    f = open('files/p096_sudoku.txt')
    a = f.readlines()
    games = getGames(a)
    output = 0
    for game in games:
        unsolved = Game(game)
        solvedGame = Solver.solve(copy.deepcopy(unsolved))
        if not (reconcile(solvedGame,unsolved) and solved(solvedGame)):
            print('Bad day')
        output += solvedGame.getAnswer()
    print("Done")
    print(output)

if __name__ == '__main__':
    solve()