import abc
from constant import SQUARE_SIZE
class pieceInterface(metaclass=abc.ABCMeta):
    def __init__(self,color,row_position,col_position):
        self.color = color
        self.row_position = row_position
        self.col_position= col_position
        self.x = 0
        self.y = 0
        if color=="white":
            self.integer_value = 1
        else:
            self.integer_value=-1
        self.calc_pos()
    #caculate the position of the x and y on the screen . 
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col_position  
        self.y = SQUARE_SIZE * self.row_position  