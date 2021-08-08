import pygame
from Board import Board
from Pond import Pond
class Game():
    def __init__(self,win):
        self.board = Board()
        self.win = win
        self.board.draw_square(self.win)
        self.board.create_board()
        self.board.draw(win)
    def update(self):
        self.board.draw_square(self.win)
        self.board.draw(self.win)
        pygame.display.update()
    def draw_square(self):
        self.board.draw_square(self.win)
    def there_is_a_piece(self,row,col):
       if self.board.board[row][col] ==0:
           return None
       return self.board.board[row][col]
    def move_piece(self,row,col,piece):
        self.board.board[piece.row_position][piece.col_position] =0
        self.board.board[row][col] = Pond("white",row,col)
         