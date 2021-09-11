import pygame
import os   
WIDTH,HEIGHT = 800,800

ROWS, COLS  = 8,8

SQUARE_SIZE = WIDTH//COLS
RED = (255,0,0)
WHITE = (255,255,255)
BLACK  = (0,0,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
LIGHT_BROWN = (224,139,62)
BRIGHT_WHITE = (251,241,231)
print("rami")

## chess
BLACK_PAWN_PATH = "./chess/assets/black_pawn.png"
WHITE_PAWN_PATH = "./chess/assets/white_pawn.png"
BLACK_PAWN = pygame.transform.scale(pygame.image.load(BLACK_PAWN_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_PAWN = pygame.transform.scale(pygame.image.load(WHITE_PAWN_PATH),(SQUARE_SIZE,SQUARE_SIZE))

## rook 
WHITE_ROOK_PATH = "./chess/assets/white_rook.png"
BLACK_ROOK_PATH = "./chess/assets/black_rook.png"
BLACK_ROOK = pygame.transform.scale(pygame.image.load(BLACK_ROOK_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_ROOK = pygame.transform.scale(pygame.image.load(WHITE_ROOK_PATH),(SQUARE_SIZE,SQUARE_SIZE))

##bishop
WHITE_BISHOP_PATH = "./chess/assets/white_bishop.png"
BLACK_BISHOP_PATH = "./chess/assets/black_bishop.png"
BLACK_BISHOP = pygame.transform.scale(pygame.image.load(BLACK_BISHOP_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load(WHITE_BISHOP_PATH),(SQUARE_SIZE,SQUARE_SIZE))

##knight
WHITE_KNIGHT_PATH = "./chess/assets/white_knight.png"
BLACK_KNIGHT_PATH = "./chess/assets/black_knight.png"
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load(BLACK_KNIGHT_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load(WHITE_KNIGHT_PATH),(SQUARE_SIZE,SQUARE_SIZE))

## queen
WHITE_QUEEN_PATH = "./chess/assets/white_queen.png"
BLACK_QUEEN_PATH = "./chess/assets/black_queen.png"
BLACK_QUEEN = pygame.transform.scale(pygame.image.load(BLACK_QUEEN_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load(WHITE_QUEEN_PATH),(SQUARE_SIZE,SQUARE_SIZE))
## king
WHITE_KING_PATH = "./chess/assets/white_king.png"
BLACK_KING_PATH = "./chess/assets/black_king.png"
BLACK_KING = pygame.transform.scale(pygame.image.load(BLACK_KING_PATH),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_KING = pygame.transform.scale(pygame.image.load(WHITE_KING_PATH),(SQUARE_SIZE,SQUARE_SIZE))


