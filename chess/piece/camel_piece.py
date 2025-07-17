from chess.piece.piece_abstract import PieceAbstract
from chess.constants import constants


class CamelPiece(PieceAbstract):
    def __init__(self, color):
        super().__init__(color)

    def get_path(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        path = []
        if to_col - from_col == to_row - from_row:  # main diagonal
            if to_col > from_col:
                for i in range(0, to_col - from_col + 1):
                    path.append((from_row + i, from_col + i))
            else:
                for i in range(0, to_col - from_col - 1, -1):
                    path.append((from_row + i, from_col + i))
            return path

        if from_row + from_col == to_row + to_col:  # other diagonal
            if to_col > from_col:  # right
                for i in range(0, to_col - from_col + 1):
                    path.append((from_row - i, from_col + i))
            else:  # left
                for i in range(0, to_col - from_col - 1, -1):
                    path.append((from_row - i, from_col + i))
            return path

        return None

    @staticmethod
    def get_type():
        return constants.PIECE_CAMEL



