import sys; sys.stdin = open('1258.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(a, b):
    visit[a][b] = True
    Q = deque()
    Q.append([a,b])
    count_x, count_y =1, 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n:
                if visit[tx][ty] == False and procession[tx][ty] != 0:
                    if dx[i] == +1:
                        count_x += 1
                    if dy[i] == +1 and tx == a:
                        count_y += 1
                    Q.append([tx, ty])
                    visit[tx][ty] = True
    # print(result)
    result.append([count_x, count_y])




T = int(input())
for tc in range(1, T+1):
    result = deque()
    n = int(input())
    procession = [list(map(int, input().split())) for i in range(n)]
    visit = [[False for _ in range(n)] for __ in range(n)]

    for x in range(n):
        for y in range(n):
            if visit[x][y] == False and procession[x][y]:
                BFS(x,y)

    for i in range(1, len(result)):
        for j in range(i, 0, -1):
            if result[j - 1][0] * result[j-1][1] > result[j][0]*result[j][1]:
                result[j], result[j - 1] = result[j - 1], result[j]
            elif result[j - 1][0] * result[j-1][1] == result[j][0]*result[j][1]:
                if result[j - 1][0] > result[j][0]:
                    result[j], result[j - 1] = result[j - 1], result[j]
    # print(result)

    for i in range(len(result)):
        result.append(' '.join(map(str, result.popleft())))
    print('#{} {} {}'.format(tc, len(result), ' '.join(result)))