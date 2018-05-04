class Vertex:
    def __init__(self, board, path, moves):
        self.board = board
        self.path = path
        self.moves = moves
        self.adjlist = []

    def boardCopy(self):
        return self.board[:]

class Queue:
    def __init__(self):
        self.l = []

    def enqueue(self, item):
        self.l.append(item)

    def dequeue(self):
        self.l.pop(0)

    def isEmpty(self):
        self.l == []

def getPossibleMoves(board):
    """
    Returns a list filled with a list of row and column integers that can be swapped.

    An example of a return value is: [[0,1],[1,2]]. In the case of [0,1], the
    element in the 0'th row and 1'st column can be swapped.
    """
    adj_list = []
    row = 0
    col = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 99:
                row = i
                col = j
                break

    if row + 1 <= 2: 
        adj_list.append([row+1, col]) #need to get rid of board

    if row - 1 >= 0:
        adj_list.append([row-1, col])

    if col + 1 <= 2: 
        adj_list.append([row, col+1])

    if col - 1 >= 0:
        adj_list.append([row, col-1])

    return adj_list
        
        
                

"""
def getStart():
    print("Enter the integers one by one row by row")
    print("")

    print("Row 1")
    row = 1
    entered = 0
    board = []
    
    while True:
        try:
            
    for i in range(9):
        if (i+1) % 3 == 0:
            row += 1
            print("Now enter Row " + row)

"""

def printPath(path, moves):
    """
    Prints the path in a block and the number of moves made
    """
    print("-" * 50)
    print("-" * 50)
    print("")
    print("Moves Made: " + str(moves))
    print("")

    if moves == 0:
        print("Already winning board")
        
           
    for i in path:
        print("Move " + str(i))
        
    print("")
    print("-" * 50)
    print("-" * 50)


if __name__ == "__main__":
    pass
