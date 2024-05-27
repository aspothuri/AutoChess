from flask import Flask, render_template, jsonify
import chess
from game import getNextMove

app = Flask(__name__)
board = chess.Board()
DEPTH = 3

@app.route('/')
def index():
    return render_template('index.html', board=board.fen())

@app.route('/get_move', methods=['GET'])
def get_move():
    global board
    best_move = getNextMove(board, DEPTH)
    if best_move is None:
        return jsonify({'move': 'Finished Execution', 'board': board.fen()})
    board.push(best_move)
    return jsonify({'move': str(best_move), 'board': board.fen()})

@app.route('/reset_board', methods=['GET'])
def reset_board():
    global board
    board = chess.Board()
    return jsonify({'message': 'Board reset successful', 'board': board.fen()})

if __name__ == '__main__':
    app.run(debug=True)
