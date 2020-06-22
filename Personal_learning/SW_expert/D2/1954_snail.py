import sys; sys.stdin = open('1954.txt', 'r')

dx = [0, +1, 0, -1]
dy = [1, 0, -1, 0]


def snail(s, n, i):
    if n == limit:
        print('#{}'.format(tc))
        for val in arr:
            print(*val)
        return
    else:
        x, y = s
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if arr[tx][ty] == 0:
                arr[tx][ty] = n
                snail((tx,ty), n+1, i)
            else:
                snail(s, n, change_direction(i))
        else:
            snail(s, n, change_direction(i))

def change_direction(i):
    if i == 3:
        return 0
    else:
        return i+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    limit = N * N + 1
    arr[0][0] = 1
    snail((0, 0), 2, 0)
