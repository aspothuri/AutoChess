import speech_recognition as sr

def identify_chess_move():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say your move:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to the user's input

    try:
        # Recognize speech using Google Speech Recognition
        move = recognizer.recognize_google(audio)
        print("You said:", move)
        return move
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def parse_chess_move(move):
    # do some regex to verify converted text (i.e bee two is b2)
    parsed_move = move.lower()  # Convert to lowercase for consistency
    return parsed_move

def validate_chess_move(move):
    # check in server to see if move is legal
    return True  # for now, just return true

# Main program
while True:
    move = identify_chess_move()
    if move:
        parsed_move = parse_chess_move(move)
        if validate_chess_move(parsed_move):
            print("Parsed move:", parsed_move)
            # send to server/serial connection
        else:
            print("Invalid move. Please try again.")
