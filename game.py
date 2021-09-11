import pygame
from Board import Board
from Pond import Pond
from Move import Move
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
    def return_a_piece_at_the_location(self,row,col):
       if self.board.board[row][col] ==0:
           return None
       return self.board.board[row][col]
    def is_there_a_piece(self,row,col):
        if self.board.board[row][col] ==0:
            return False
        return True    
    def moves(self,selected_piece):
        list_of_valid_moves = []
        ## if pond just started
        if selected_piece.piece == "pond":
            if selected_piece.row_position == 1 or selected_piece.row_position == 6:
                if selected_piece.color=="white" and self.valid_move(selected_piece,2,0):
                    print("action")
                    list_of_valid_moves.append(Move(selected_piece,selected_piece.row_position+2,selected_piece.col_position,None))
                elif selected_piece.color=="black" and self.valid_move(selected_piece,-2,0):
                    list_of_valid_moves.append(Move(selected_piece,selected_piece.row_position-2,selected_piece.col_position,None))
            if selected_piece.color=="white" and  self.valid_move(selected_piece,1,0):
                    list_of_valid_moves.append(Move(selected_piece,selected_piece.row_position+1,selected_piece.col_position,None))
            elif selected_piece.color == "black" and self.valid_move(selected_piece,-1,0):
                    list_of_valid_moves.append(Move(selected_piece,selected_piece.row_position-1,selected_piece.col_position,None))
        return list_of_valid_moves
    def valid_move(self,piece,row,col):
        ## logic for a pong
        if piece.piece == "pond" and piece.row_position+row>=0 and piece.row_position +row <=7 and piece.col_position+col>=0 and piece.col_position+col<=7 and not self.is_there_a_piece(row+piece.row_position,col+piece.col_position):
            return True
        return False
    def is_selected_move_valid(self,row,col,piece):
        the_list = self.moves(piece)
        print(the_list)
        for x in the_list:
            if x.new_row == row:
                if x.new_col ==col:
                    if x.current_piece.color == piece.color:
                        if x.current_piece.piece == piece.piece:
                            return True
        return False
    def move_piece(self,row,col,piece):
        self.board.board[piece.row_position][piece.col_position] =0
        self.board.board[row][col] = self.add_new_piec(row,col,piece)
    def add_new_piec(self,row,col,piece):
        if(piece.piece=="pond"):
            return Pond(piece.color,row,col)
        return None
         