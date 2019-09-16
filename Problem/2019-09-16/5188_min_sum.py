import sys; sys.stdin = open('5188.txt', 'r')
from collections import deque

dx = [0, +1]
dy = [+1, 0]

def BFS(s):
    Q = deque()
    Q.append(s)
    while Q:
        x, y = Q.popleft()
        for i in range(2):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                num = check[x][y] + arr[tx][ty]
                if check[tx][ty] > num:
                    check[tx][ty] = num
                    Q.append([tx,ty])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [[10000 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    check[0][0] = arr[0][0]
    BFS([0,0])
    print('#{} {}'.format(tc, check[N-1][N-1]))
