import sys; sys.stdin = open('2178.txt', 'r')
from collections import deque

dx =[-1, +1, 0, 0]
dy =[0, 0, -1, +1]


def BFS(s, arrival):
    # print(arrival)
    visit[s[0]][s[1]]
    Q = deque()
    Q.append(s)
    D[s[0]][s[1]] = 1
    P[s[0]][s[1]] = s
    while Q:
        v = Q.popleft()
        for w in range(4):
            x = v[0] + dx[w]
            y = v[1] + dy[w]
            # print(x,y)
            if 0 <= x < N and 0 <= y < M:
                # print(x,y)
                if not visit[x][y] and maze[x][y] == 1:
                    visit[x][y] = True
                    # print([x,y], v, D[x][x])
                    D[x][y] = D[v[0]][v[1]] + 1
                    P[x][y] = [x, y]
                    Q.append([x, y])
                if x == arrival[0] and y == arrival[1]:
                    print(D[x][y])
                    return




start = [0, 0]
N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]
visit = [[False for _ in range(M)] for __ in range(N)]
D = [[0 for _ in range(M)] for __ in range(N)]
P = [[[] for _ in range(M)] for __ in range(N)]
# print(maze)
BFS(start, [N-1, M-1])
# print(D)
# print(P)