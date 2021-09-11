from dataclasses import dataclass
from PieceInterface import pieceInterface
@dataclass
class Move:
    current_piece: pieceInterface
    new_row: int
    new_col: int
    piece_taken: pieceInterface