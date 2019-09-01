import sys; sys.stdin = open('2205.txt', 'r')
from collections import deque

dx =[-1, +1, 0, 0]
dy =[0, 0, -1, +1]

def DFS(x, y, check, visit, repeat):
    visit[x][y] = True
    print(x, y)
    print(check)
    if x == N-1 and y == M-1:
        print(check)
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        # print(x,y, tx,ty, visit[tx][ty], maze[tx][ty],repeat)
        if 0 <= tx < N and 0 <= ty < M and visit[tx][ty] == False and maze[tx][ty] == 0:
            # print('13131')
            check += 1
            DFS(tx, ty, check, visit, repeat)
        elif 0 <= tx < N and 0 <= ty < M and visit[tx][ty] == False and maze[tx][ty] == 1 and repeat == 1:
            repeat = 0
            check += 1
            DFS(tx, ty, check, visit, repeat)
            repeat = 1






start = [0, 0]
N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]
visits = [[False for _ in range(M)] for __ in range(N)]
D = [[10000 for _ in range(M)] for __ in range(N)]
DFS(0, 0, 1, visits, 1)