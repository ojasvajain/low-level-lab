
from board import Board
from constants import constants


def main():
    b = Board()
    b.show_board()
    b.move_piece(constants.COLOR_WHITE, (6,1), (5,1))
    b.show_board()
    b.move_piece(constants.COLOR_BLACK, (1,0), (2,0))
    b.show_board()
    b.move_piece(constants.COLOR_WHITE, (7,2), (5,0))
    b.show_board()
    b.move_piece(constants.COLOR_BLACK, (2, 0), (3, 0))
    b.show_board()
    b.move_piece(constants.COLOR_WHITE, (5,0), (1,4))
    b.show_board()
    b.move_piece(constants.COLOR_BLACK, (0,4), (1, 4))
    b.show_board()


if __name__ == '__main__':
    main()

