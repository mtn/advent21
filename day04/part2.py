
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

remaining = set(range(len(boards)))
called = nums[:5]
for num in nums[5:]:
    for i, board in enumerate(boards):
        if i not in remaining:
            continue

        rowres = check_rows(board, called)
        colres = check_cols(board, called)

        if rowres is not None or colres is not None:
            remaining.remove(i)

        if len(remaining) == 0:
            res = rowres or colres
            print(res)
            exit()

    called.append(num)
