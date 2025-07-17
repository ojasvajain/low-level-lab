from piece import camel_piece, elephant_piece, horse_piece, king_piece, queen_piece, soldier_piece
from constants import constants


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(constants.GRID_SIZE)] for _ in range(constants.GRID_SIZE)]
        self.dead_pieces = {
            constants.COLOR_WHITE: [],
            constants.COLOR_BLACK: []
        }

        self.turn = constants.COLOR_WHITE
        self.__init_white_player_pieces()
        self.__init_black_player_pieces()

    def __init_black_player_pieces(self):
        self.grid[0][0] = elephant_piece.ElephantPiece(constants.COLOR_BLACK)
        self.grid[0][7] = elephant_piece.ElephantPiece(constants.COLOR_BLACK)

        self.grid[0][1] = horse_piece.HorsePiece(constants.COLOR_BLACK)
        self.grid[0][6] = horse_piece.HorsePiece(constants.COLOR_BLACK)

        self.grid[0][2] = camel_piece.CamelPiece(constants.COLOR_BLACK)
        self.grid[0][5] = camel_piece.CamelPiece(constants.COLOR_BLACK)

        self.grid[0][3] = king_piece.KingPiece(constants.COLOR_BLACK)
        self.grid[0][4] = queen_piece.QueenPiece(constants.COLOR_BLACK)

        for i in range(0, 8):
            self.grid[1][i] = soldier_piece.SoldierPiece(constants.COLOR_BLACK)

    def __init_white_player_pieces(self):
        self.grid[7][0] = elephant_piece.ElephantPiece(constants.COLOR_WHITE)
        self.grid[7][7] = elephant_piece.ElephantPiece(constants.COLOR_WHITE)

        self.grid[7][1] = horse_piece.HorsePiece(constants.COLOR_WHITE)
        self.grid[7][6] = horse_piece.HorsePiece(constants.COLOR_WHITE)

        self.grid[7][2] = camel_piece.CamelPiece(constants.COLOR_WHITE)
        self.grid[7][5] = camel_piece.CamelPiece(constants.COLOR_WHITE)

        self.grid[7][3] = king_piece.KingPiece(constants.COLOR_WHITE)
        self.grid[7][4] = queen_piece.QueenPiece(constants.COLOR_WHITE)

        for i in range(0, 8):
            self.grid[6][i] = soldier_piece.SoldierPiece(constants.COLOR_WHITE)

    def move_piece(self, player_color, from_pos, to_pos):
        if player_color != self.turn:
            raise Exception(f"It is not {player_color}\'s turn")

        if from_pos[0] < 0 or from_pos[0] >= constants.GRID_SIZE or from_pos[1] < 0 or from_pos[1] >= constants.GRID_SIZE:
            raise Exception('Invalid start position')

        if to_pos[0] < 0 or to_pos[0] >= constants.GRID_SIZE or to_pos[1] < 0 or to_pos[1] >= constants.GRID_SIZE:
            raise Exception('Invalid to position')

        if from_pos == to_pos:
            raise Exception('Start position is same as End position')

        dest_piece = self.grid[to_pos[0]][to_pos[1]]
        if dest_piece is not None and dest_piece.color == player_color:
            raise Exception('To position contains piece of same color')

        source_piece = self.grid[from_pos[0]][from_pos[1]]
        if source_piece is None:
            raise Exception('Start position does not contain any piece')

        # Check if piece present on pos belongs to the same color
        if source_piece.color != player_color:
            raise Exception('Piece does not belong to the color provided')

        # If source piece is a soldier and there is an opponent diagonally
        # soldier is allowed to move

        # Check if it is feasible to move from from_pos to to_pos
        path = source_piece.get_path(from_pos, to_pos)
        if path is None:
            raise Exception(f'Invalid to move {source_piece.get_type()} from {from_pos} to {to_pos}')

        # Check if there is any piece along the path, if yes, return error
        # Exclude current cell and last cell
        for cell in path[1:-1]:
            row, col = cell
            if self.grid[row][col] is not None:
                raise Exception(f'Not possible to move {source_piece.get_type()} from {from_pos} to {to_pos} as '
                                f'there is a piece at {row},{col}')

        if dest_piece is not None:
            # this piece will be eliminated
            self.dead_pieces[dest_piece.color].append(dest_piece)
            print(f'{dest_piece.get_type()} of color {dest_piece.color} has been eliminated')

        # update the grid
        self.grid[to_pos[0]][to_pos[1]] = source_piece
        self.grid[from_pos[0]][from_pos[1]] = None
        print(f'{source_piece.get_type()} of color {source_piece.color} moved from {from_pos} to {to_pos}')

        if self.turn == constants.COLOR_WHITE:
            self.turn = constants.COLOR_BLACK
        else:
            self.turn = constants.COLOR_WHITE

    def show_board(self):
        for i in range(constants.GRID_SIZE):
            row_str = ""
            for j in range(constants.GRID_SIZE):
                piece = self.grid[i][j]
                if piece is None:
                    row_str += ".."
                else:
                    row_str += piece.get_type().upper()[0] + piece.color
                row_str += "  "
            print(row_str)

        print('\nDead Pieces:')
        for key in self.dead_pieces:
            print(f'{key} - {[v.get_type() for v in self.dead_pieces[key]]}')


