import sys; sys.stdin = open('5250.txt', 'r')
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(s):
    Q= deque()
    Q.append(s)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if arr[tx][ty] > arr[x][y]:
                    cost = abs(arr[tx][ty] - arr[x][y]) + 1 + cost_arr[x][y]
                else:
                    cost = 1 + cost_arr[x][y]
                if cost_arr[tx][ty] > cost:
                    cost_arr[tx][ty] = cost
                    Q.append((tx, ty))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost_arr = [[0xffffff for _ in range(N)] for _ in range(N)]
    cost_arr[0][0] = 0
    BFS((0,0))
    N -= 1
    print('#{} {}'.format(tc, cost_arr[N][N]))
