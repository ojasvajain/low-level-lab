from chess.piece.piece_abstract import PieceAbstract
from chess.piece.camel_piece import CamelPiece
from chess.piece.elephant_piece import ElephantPiece
from chess.constants import constants


class QueenPiece(PieceAbstract):
    def __init__(self, color):
        super().__init__(color)

    def get_path(self, from_pos, to_pos):
        camel_path = CamelPiece(self.color).get_path(from_pos, to_pos)
        if camel_path is not None:
            return camel_path

        elephant_path = ElephantPiece(self.color).get_path(from_pos, to_pos)
        if elephant_path is not None:
            return elephant_path

        return None

    @staticmethod
    def get_type():
        return constants.PIECE_QUEEN