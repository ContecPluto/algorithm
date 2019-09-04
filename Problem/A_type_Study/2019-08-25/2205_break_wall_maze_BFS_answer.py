import sys; sys.stdin = open('2205.txt', 'r')
from collections import deque

dx =[-1, +1, 0, 0]
dy =[0, 0, -1, +1]


def BFS(s, arrival):
    # print(arrival)
    visit[s[0]][s[1]] = True
    Q = deque()
    Q.append(s)
    D[0][0][0] = 1
    while Q:
        x, y, z = Q.popleft()
        if x == N - 1 and y == M - 1:
            ans = D[x][y][w]
            break
        for w in range(4):
            tx = x + dx[w]
            ty = y + dy[w]
            # print(x,y)
            if 0 < x <= N and 0 < y <= M:
                # print(x,y)
                if D[tx][ty][z]:  # 길
                    continue

                if maze[x][y] == 0:
                    D[tx][ty][z] = D[x][y][z] + 1
                    Q.append((tx, ty, z))
                elif z == 0:
                    D[tx][ty][1] = D[x][y][w] + 1
                    Q.append((tx, ty, 1))
    else:
        ans = -1




ans = 0
start = [0, 0]
N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]
visit = [[False for _ in range(M)] for __ in range(N)]
D = [[[0, 0] for _ in range(M)] for __ in range(N)]
# print(maze)
BFS((0,0,0), [N-1, M-1] )
print(ans)
print(D)