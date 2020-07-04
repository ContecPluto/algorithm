# https://www.acmicpc.net/problem/2580

def block(x, y):
    array = [0] * 10
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            array[sudoku[i][j]] += 1
    return array


def check_sudoku(index):
    global answer
    if answer:
        if index == N:
            for line in sudoku:
                print(*line)
            answer = False
            return
        x, y = zeros[index]
        blcok_check = block(x//3, y//3)
        for i in range(1, 10):
            if sudoku_count_x[x][i] == 0 and sudoku_count_y[y][i] == 0 and blcok_check[i] == 0:
                sudoku_count_x[x][i] += 1
                sudoku_count_y[y][i] += 1
                sudoku[x][y] = i
                check_sudoku(index + 1)
                sudoku[x][y] = 0
                sudoku_count_x[x][i] -= 1
                sudoku_count_y[y][i] -= 1
        
        
sudoku = [list(map(int, input().split(" "))) for _ in range(9)]
zeros = []
sudoku_count_x = [[0]* 10 for _ in range(9)]
sudoku_count_y = [[0]* 10 for _ in range(9)]
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            zeros.append([x, y])
        sudoku_count_x[x][sudoku[x][y]] += 1
        sudoku_count_y[x][sudoku[y][x]] += 1
N = len(zeros)
answer = True
check_sudoku(0)