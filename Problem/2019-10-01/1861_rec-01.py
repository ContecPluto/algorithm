import sys; sys.stdin = open('1861.txt', 'r')
from collections import deque
sys.setrecursionlimit(99999999)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(s):
    global check
    Q = deque()
    Q.append(s)
    # print(s)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if arr[tx][ty] - arr[x][y] == 1 and visit[tx][ty] < visit[x][y] + 1:
                    visit[tx][ty] = visit[x][y] + 1
                    Q.append([tx,ty])
    check=[x,y]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [9999999, 2]
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[1 for _ in range(N)] for _ in range(N)]

    for a in range(N):
        for b in range(N):
            check = [0, 0]
            BFS([a, b])
            x, y = check
            if visit[x][y] > result[1]:
                result[1] = visit[x][y]
                result[0] = arr[a][b]
            elif visit[x][y] == result[1]:
                result[1] = visit[x][y]
                result[0] = min(arr[a][b], result[0])
    print('#{} {} {}'.format(tc, *result))


