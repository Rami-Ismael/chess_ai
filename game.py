import pygame
from Board import Board
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
        self.board.draw_square(self.win)
        self.board.create_board()
        self.board.draw(win)
    def update(self):
        pygame.display.update()
    def draw_square(self):
        self.board.draw_square(self.win)
         