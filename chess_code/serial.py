from game import getNextMove
import chess

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with your port name

board = chess.Board()

DEPTH = 3

while True:
    move = str(getNextMove(board, DEPTH))
    board.push(move)
    # Write data to C++
    ser.write(move.encode())

    # Read data from C++
    data = ser.readline().decode().strip()
    board.push(data)
