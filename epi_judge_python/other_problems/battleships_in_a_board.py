# Given an 2D board, count how many battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.

# You may assume the following rules:
# - You receive a valid board, made of only battleships or empty slots.
# - Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# - At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

def countBattleships(board) -> int:
    def check_position_contains_ship(row_i, col_j, board):
        return 0 <= row_i < len(board) and 0 <= col_j < len(board[row_i]) and board[row_i][col_j] == 'X'

    result = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                possible_directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                direction = None
                for possible_direction in possible_directions:
                    potential_i = i + possible_direction[0]
                    potential_j = j + possible_direction[1]

                    if check_position_contains_ship(potential_i, potential_j, board):
                        direction = possible_direction
                        break

                if direction:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    while check_position_contains_ship(new_i, new_j, board):
                        board[new_i][new_j] = 'O'
                        new_i += direction[0]
                        new_j += direction[1]

                board[i][j] = 'O'
                result += 1

    return result


if __name__ == '__main__':
    from pprint import pprint

    # boards = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    boards = [["X", "X", "X"]]
    for board in boards:
        print(board)

    result = countBattleships(boards)
    print(result)
