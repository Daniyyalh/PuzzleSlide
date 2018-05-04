
def play():
    seen = {} # board : numberofMoves
    win_board = [[1,2,3],[4,5,6],[7,8,9]]
    
    q = Queue()
    
    initial_board = getStart()
    v = Vertex(initial_board, [], 0)

    seen[tuple(initial_board)] = 0
    q.enqueue(initial_board)

    while not q.isEmpty():
        curr = q.dequeue()

        if curr.board == board:
            printPath(curr.path, curr.moves)
            break

        adj_list = getPossibleMoves(curr.board)

        for i in adj_list:
            to_move = Vertex(curr.board, path,         


            if to_move.board in seen:
                if seen[to_move.board] < curr.moves:
                    pass

                else:
                    seen[to_move.board] = moves
                    q.enqueue(to_move)
                

    







if __name__ == "__main__":
    play()
