import pygame
import chess
import chess.svg

#constants
WHITE = (255, 253, 208)
BLACK = (150, 75, 0)

SQUARE_SIZE = 60
BOARD_SIZE = 8

PIECE_SIZE = 60
OFFSET_X = (SQUARE_SIZE - PIECE_SIZE) // 2
OFFSET_Y = (SQUARE_SIZE - PIECE_SIZE) // 2

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# piece_images file paths
piece_images = {
    'r': 'piece_images/black_rook.png',
    'n': 'piece_images/black_knight.png',
    'b': 'piece_images/black_bishop.png',
    'q': 'piece_images/black_queen.png',
    'k': 'piece_images/black_king.png',
    'p': 'piece_images/black_pawn.png',
    'R': 'piece_images/white_rook.png',
    'N': 'piece_images/white_knight.png',
    'B': 'piece_images/white_bishop.png',
    'Q': 'piece_images/white_queen.png',
    'K': 'piece_images/white_king.png',
    'P': 'piece_images/white_pawn.png'
}

def render(board):
    # Initialize Pygame
    pygame.init()

    # Set up the display
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chess Board")

    def draw_board():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # piece = board[row][col]
                square = chess.square(col, 7 - row)
                piece = board.piece_at(square)
                if piece is not None:
                    piece_image = pygame.image.load(piece_images[piece.symbol()])
                    screen.blit(piece_image, (col*SQUARE_SIZE, row*SQUARE_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)  # Fill the screen with white
        draw_board()        # Draw the chess board
        draw_pieces()       # Draw the chess pieces
        pygame.display.flip()  # Update the display

    pygame.quit()

# board = chess.Board()
# render(board)