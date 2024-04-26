import chess
from render import render

board = chess.Board()

board.set_piece_at(chess.E4, chess.Piece(chess.PAWN, chess.WHITE))
render(board)

