from PieceInterface import pieceInterface
from constant import WHITE_PAWN
class Pond(pieceInterface):
    def __init__(self,color,row_position,col_position):
        super().__init__(color,row_position,col_position,"pond")
    def movement(self,board):
        return ((1,0))
    def draw(self,win):
        if self.color =="white":
            win.blit(WHITE_PAWN,(self.x,self.y))