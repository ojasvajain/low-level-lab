from chess.piece.piece_abstract import PieceAbstract
from chess.constants import constants


class SoldierPiece(PieceAbstract):
    def __init__(self, color):
        super().__init__(color)

    def get_path(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if from_col == to_col and abs(from_row - to_row) == 1:
            if self.color == constants.COLOR_BLACK and to_row > from_row:
                return [from_pos, to_pos]
            if self.color == constants.COLOR_WHITE and to_row < from_row:
                return [from_pos, to_pos]

        return None

    @staticmethod
    def get_type():
        return constants.PIECE_SOLDIER
