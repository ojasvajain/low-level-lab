from abc import ABC
from chess.piece.piece_abstract import PieceAbstract
from chess.constants import constants


class ElephantPiece(PieceAbstract):
    def __init__(self, color):
        super().__init__(color)

    def get_path(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        path = []
        if from_row == to_row:  # horizontal
            if to_col > from_col:  # right
                for i in range(0, to_col - from_col + 1):
                    path.append((from_row, from_col + i))
            else:  # left
                for i in range(0, from_col - to_col + 1):
                    path.append((from_row, from_col - i))
            return path

        if from_col == to_col:  # vertical
            if to_row > from_row:  # down
                for i in range(0, to_row - from_row + 1):
                    path.append((from_row + i, from_col))
            else:  # up
                for i in range(0, from_row - to_row + 1):
                    path.append((from_row - i, from_col))
            return path

        return None

    @staticmethod
    def get_type():
        return constants.PIECE_ELEPHANT