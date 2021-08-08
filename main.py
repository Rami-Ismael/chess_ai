#import

import pygame
from constant import WIDTH,HEIGHT, SQUARE_SIZE
from game import Game

FPS = 60
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")
def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run=True
    clock = pygame.time.Clock()
    game = Game(win)
    selected_piece = []
    turn = "white"
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                print(row,col)
                piece  = game.there_is_a_piece(row,col)
                if piece is not None and piece.color==turn:
                    if len(selected_piece):
                        selected_piece.pop()
                    selected_piece.append(piece)
                ## move the selected peice 
                elif len(selected_piece)==1:
                     game.move_piece(row,col,selected_piece.pop())
        game.update()
    

main()
            