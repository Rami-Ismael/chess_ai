from constant import BRIGHT_WHITE,ROWS,COLS,LIGHT_BROWN,SQUARE_SIZE
import pygame
WHITE_SECTION = "white"
BLACK_SECTION = "black"
from Pond import Pond
class Board:
    def __init__(self):
        self.board = []
    def draw_square(self,win):
        for row in range(ROWS):
            for col in range(COLS):
                if row %2 ==0 and col%2==0:
                    pygame.draw.rect(win,LIGHT_BROWN,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
                elif row%2 ==0 and col%2==1:
                    pygame.draw.rect(win,BRIGHT_WHITE,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
                if row %2 ==1 and col%2==0:
                    pygame.draw.rect(win,BRIGHT_WHITE,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
                elif row %2 ==1 and col%2==1:
                    pygame.draw.rect(win,LIGHT_BROWN,((row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)))
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row ==1:
                    self.board[row].append(Pond(WHITE_SECTION,row,col))
                else:
                    self.board[row].append(0)
    def draw(self,win):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(win)