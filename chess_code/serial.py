from game import getNextMove
import chess
import serial
from ..speech_recognition_code.speech import identify_chess_move

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with your port name

board = chess.Board()

DEPTH = 3

audio_data = []

try:
    while True:
        move = str(getNextMove(board, DEPTH))
        board.push(move)
        # Write data to C++
        ser.write(move.encode())

        # Read data from C++
        data = ser.readline().decode().strip()
        board.push(data)

        line = ser.readline().decode('utf-8').rstrip()
        mic_value = int(line)
        audio_data.append(mic_value)
        print(mic_value)  # Print to verify the data
except KeyboardInterrupt:
    print("Program interrupted by user")

# save audio to file
with open('audio_data.txt', 'w') as file:
    for value in audio_data:
        file.write(f"{value}\n")

# do stuff with the speech_recognition_code
