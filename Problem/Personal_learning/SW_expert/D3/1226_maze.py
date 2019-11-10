import sys; sys.stdin = open('1226.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def DFS(s):
    global result
    x, y = s
    arr[x][y] = 9
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 16 and 0 <= ty < 16:
            if arr[tx][ty] == 0:
                DFS([tx, ty])
            elif arr[tx][ty] == 3:
                result = 1
                return

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    result = 0
    for i in range(16):
        if 2 in arr[i]:
            idx = arr[i].index(2)
            DFS([i, idx])
            break
    print('#{} {}'.format(tc, result))