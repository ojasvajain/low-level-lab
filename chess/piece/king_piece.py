from chess.piece.piece_abstract import PieceAbstract
from chess.constants import constants


class KingPiece(PieceAbstract):
    def __init__(self, color):
        super().__init__(color)

    def get_path(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        if abs(to_col - from_col) <= 1 and abs(to_row - from_row) <= 1:
            return [from_pos, to_pos]

        return None

    @staticmethod
    def get_type():
        return constants.PIECE_KING







