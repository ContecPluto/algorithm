def DFS(x, y):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    global apart, cnt
    # print(x,y)
    apart[x][y] = 0
    cnt += 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        # print(tx, ty)
        if 0 <= tx <= (N - 1) and 0 <= ty <= (N - 1):
            # print(tx,ty)
            if apart[tx][ty]:
                DFS(tx, ty)

import sys; sys.stdin = open('2667.txt', 'r')
N = int(input())
apart = [list(map(int, (map(str, input())))) for _ in range(N)]

cnt = 0
check = []

for x in range(N):
    for y in range(N):
        if apart[x][y]:
            DFS(x, y)
            check.append(cnt)
            cnt = 0
check.sort()
print(len(check))
for i in range(len(check)):
    print(check[i])

