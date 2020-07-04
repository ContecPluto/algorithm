# https://www.acmicpc.net/problem/2580
def block(x, y):
    array = []
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if sudoku[i][j] == 0: continue
            array.append(sudoku[i][j])
    return array


def check(index):
    global answer
    if answer:
        if index == N:
            print()
            for line in sudoku:
                print(*line)
            answer = False
            return
        x, y = zeros[index]
        blcok_check = set(range(1, 10)) - set(block(x//3, y//3))
        cross_val = blcok_check & sudoku_count_x[x] & sudoku_count_y[y]
        for val in cross_val:
            sudoku[x][y] = val
            sudoku_count_x[x].remove(val)
            sudoku_count_y[y].remove(val)
            check(index + 1)
            sudoku_count_x[x].add(val)
            sudoku_count_y[y].add(val)
            sudoku[x][y] = 0



sudoku = [list(map(int, input().split(" "))) for _ in range(9)]
sudoku_count_x = [[] for _ in range(9)]
sudoku_count_y = [[] for _ in range(9)]
zeros = []
answer = True
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            zeros.append([x, y])
        sudoku_count_x[x].append(sudoku[x][y])
        sudoku_count_y[x].append(sudoku[y][x])
N = len(zeros)

origin = set(range(10))
for x in range(9):
    sudoku_count_x[x] = origin - set(sudoku_count_x[x])
    sudoku_count_y[x] = origin - set(sudoku_count_y[x])
check(0)