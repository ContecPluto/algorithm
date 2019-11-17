import sys; sys.stdin = open('1249.txt', 'r')
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def BFS(s):
    Q = deque()
    Q.append(s)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if count[tx][ty] > count[x][y] + arr[tx][ty]:
                    count[tx][ty] = count[x][y] + arr[tx][ty]
                    Q.append([tx, ty])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    count = [[0xfffff] * N for _ in range(N)]
    count[0][0] = arr[0][0]
    BFS([0, 0])
    print('#{} {}'.format(tc, count[N-1][N-1]))

