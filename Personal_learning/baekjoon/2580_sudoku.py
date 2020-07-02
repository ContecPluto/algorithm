# https://www.acmicpc.net/problem/2580

# def line_x(num, val):
#     # 가로축 val가 있는지 확인
#     for i in range(9):
#         if sudoku[num][i] == val:
#             return False
#     return True


# def line_y(num, val):
#     # 세로축 val가 있는지 확인
#     for i in range(9):
#         if sudoku[i][num] == val:
#             return False
#     return True


def block(x, y, val):
    # 구역별 val 이 있는지 확인
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if sudoku[i][j] == val:
                return False
    return True


# def move(spot):
#     x, y = spot
#     y += 1
#     if y == 9:
#         x += 1
#         y = 0
#     return [x, y]


def check_sudoku(index):
    global answer
    if answer:
        if index == len(zeros):
            for line in sudoku:
                print(*line)
            answer = False
            return
        x, y = zeros[index]
        if sudoku[x][y] == 0:
            for i in range(1, 10):
                if sudoku_count_x[x][i] == 0 and sudoku_count_y[y][i] == 0 and block(x//3, y//3, i):
                    sudoku_count_x[x][i] += 1
                    sudoku_count_y[y][i] += 1
                    sudoku[x][y] = i
                    check_sudoku(index + 1)
                    sudoku[x][y] = 0
                    sudoku_count_x[x][i] -= 1
                    sudoku_count_y[y][i] -= 1
        else:
            check_sudoku(index + 1)
        
        
sudoku = [list(map(int, input().split(' '))) for _ in range(9)]
zeros = []
sudoku_count_x = [[0]* 10 for _ in range(9)]
sudoku_count_y = [[0]* 10 for _ in range(9)]
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            zeros.append([x, y])
        sudoku_count_x[x][sudoku[x][y]] += 1
        sudoku_count_y[x][sudoku[y][x]] += 1
answer = True
check_sudoku(0)