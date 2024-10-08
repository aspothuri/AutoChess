import chess
import chess.polyglot
from render import render

# piece position tables (derived from chess theory)
piece_tables = {
    "p": [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0],

    'n': [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50],

    "b": [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20],

    "r": [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0],

    "q": [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20],

    "k": [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30]
}


def eval(board):
    # edge cases (i.e. checkmate, draw, etc.)
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    # material score calculation
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material_score = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

    # strategic score calculation
    strategy_score = 0
    for square, piece in board.piece_map().items():
        piece_type = piece.symbol().lower()
        if piece.color == chess.WHITE:
            strategy_score += piece_tables[piece_type][square]
        else:
            strategy_score -= piece_tables[piece_type][chess.square_mirror(square)]

    total_score = (material_score + strategy_score)

    if board.turn:
        return total_score
    else:
        return -total_score

def minimax(board_state, depth, alpha, beta, whites_turn):
    if depth == 0 or board_state.is_game_over():
        return eval(board_state), None

    if whites_turn:
        max_eval = -10000
        best_move = None
        for move in board_state.legal_moves:
            new_board_state = board_state.copy()
            new_board_state.push(move)

            curr_eval, _ = minimax(new_board_state, depth - 1, alpha, beta, not whites_turn)
            if curr_eval > max_eval:
                max_eval = curr_eval
                best_move = move

            alpha = max(alpha, curr_eval)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = 10000
        best_move = None
        for move in board_state.legal_moves:
            new_board_state = board_state.copy()
            new_board_state.push(move)

            curr_eval, _ = minimax(new_board_state, depth - 1, alpha, beta, not whites_turn)
            if curr_eval < min_eval:
                min_eval = curr_eval
                best_move = move

            beta = min(beta, curr_eval)
            if beta <= alpha:
                break

        return min_eval, best_move


def getNextMove(board, depth):
    try:
        move = chess.polyglot.MemoryMappedReader("./training_files/human.bin").weighted_choice(board).move
        return move
    except Exception as e:
        return minimax(board, depth, -10000, 10000, False)[1]




# print("current score: ", eval(board))

# render(board)
