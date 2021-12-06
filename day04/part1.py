with open("input.txt") as f:
    lines = f.read().strip().split("\n\n")

nums = list(map(int, lines[0].split(",")))

board_inp = lines[1:]

boards = []
for bi in board_inp:
    boards.append([list(map(int, x.split())) for x in bi.split("\n")])

def compute_score(board, called):
    flat_board = [x for row in board for x in row]
    called_sum = sum(x for x in flat_board if x not in called)
    return called_sum * called[-1]

def check_rows(board, called):
    for row in board:
        row = set(row)
        if row.issubset(set(called)):
            return compute_score(board, called)

def check_cols(board, called):
    for col_ind in range(len(board[0])):
        col = set(r[col_ind] for r in board)
        if col.issubset(set(called)):
            return compute_score(board, called)

called = nums[:5]
for num in nums[5:]:
    for board in boards:
        rowres = check_rows(board, called)

        if rowres is not None:
            print(rowres)
            exit()

        colres = check_cols(board, called)

        if colres is not None:
            print(colres)
            exit()

    called.append(num)


# called = [10, 83, 98, 12, 33]
# print(boards[0])
