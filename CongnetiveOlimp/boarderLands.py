board_side_length, row_for_summing = int(input()), int(input())

board = [[None for _ in range(board_side_length)] for _ in range(board_side_length)]

max_digit = (board_side_length ** 2) // 2 if board_side_length % 2 == 0 else (board_side_length  ** 2) // 2 + 1

count = 1

for x in range(1, board_side_length + 1):
    for y in range(1, board_side_length, 2):
        board[x - 1][y - 1] = count
        board[x - 1][y] = max_digit + count
        count += 1
    if board_side_length % 2 == 1:
        board[x - 1][-1] = count if x % 2 != 0 else count + max_digit
        count += 1

for a in board:
    print(a)
print(sum(board[row_for_summing - 1]))