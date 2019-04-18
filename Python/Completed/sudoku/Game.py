
class Game:
    def __init__(self,matrix):
        self.cells = []
        self.board = []
        for i in range(len(matrix)):
            current = []
            for j in range(len(matrix[i])):
                cell = Cell(self,matrix[i][j], i, j)
                current.append(cell)
                self.cells.append(cell)
            self.board.append(current)


    def getCell(self ,row ,col):
        return self.board[row][col]

    def getRow(self, row):
        return self.board[row]

    def getColumn(self, col):
        return [row[col] for row in self.board]

    def getBlock(self,row,col):
        cells = []
        for i in range(row * 3,row * 3 + 3):
            for j in range(col * 3, col * 3 + 3):
                cells.append(self.board[i][j])
        return cells

    def getAnswer(self):
        output = 0
        output += self.board[0][0].value * 100
        output += self.board[0][1].value * 10
        output += self.board[0][2].value
        return output


    def __iter__(self):
        return self.cells.__iter__()

    def __len__(self):
        return self.cells.__len__()

class Cell:
    def __init__(self, game, value, row, col):
        self.game = game
        self.value = int(value)
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

    def getRow(self):
        return self.game.getRow(self.row)

    def getColumn(self):
        return self.game.getColumn(self.col)

    def getBlock(self):
        row = self.row // 3
        col = self.col // 3
        return self.game.getBlock(row,col)

