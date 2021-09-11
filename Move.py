from dataclass import Dataclass
from PieceInterface import pieceInterface
class Move():
    current_piece: pieceInterface
    new_row: int
    new_col: int
    piece_taken: pieceInterface