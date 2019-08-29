import sys; sys.stdin = open('1974.txt', 'r')

T = int(input())
for tc in range(1, 11):
    result=1
    sdoku = [list(map(int, input().split())) for x in range(9)]

    for x in range(9):
        x_check = sum(sdoku[x])
        if x_check != 45:
            result = 0
            break

        y_check = 0
        for y in range(9):
            y_check += sdoku[y][x]
        if y_check != 45:
            result = 0
            break

    for x in range(0,9,3):
        for y in range(0,9,3):
            check = 0
            for z in range(3):
                for k in range(3):
                    # print(x+z, y+k)
                    check += sdoku[x+z][k+y]
            if check != 45:
                result = 0
                break
        if check != 45:
            result = 0
            break
    print('#{} {}'.format(tc, result))


