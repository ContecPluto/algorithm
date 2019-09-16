import sys; sys.stdin = open('5186.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    x = float(input())
    check = []
    result = ''
    for j in range(-1, -13, -1):
        if x >= (2**j):
            x -= (2**j)
            result += '1'
        else:
            result += '0'
        if x == 0:
            break
    if x != 0:
        result = 'overflow'
    print('#{} {}'.format(tc, result))