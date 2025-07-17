
1. 2 players, 1 chess board, one game at a time
2. players can make their moves
3. in the end one player wins


entities
1. game, board, players, piece
2. game -> board + players
3. board -> pieces


Methods
1. Game Class
    - init() - initializes fresh board and players
    - play(player_id, move) - play a particular move. Return failure if it was invalid.
      - do check for checkmate
      - print killed pieces

2. Board
   - init() - init fresh board with pieces at their default position
   - move_piece() - move a piece from pos1 to pos2, return error if not possible
   - show_board() - print the current state of board
   - 