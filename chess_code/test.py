from game import getNextMove
import chess
from render import render
from game import eval


# testing

# initialize board
board = chess.Board()

DEPTH = 3
NUM_MOVES = 50
for i in range(0, NUM_MOVES):
    render(board)
    best_move = getNextMove(board, DEPTH)
    if best_move is None:
        print("Finished Execution")
        break
    print("best move: ", best_move)
    print(eval(board))
    board.push(best_move)