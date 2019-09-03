import sys; sys.stdin = open('2205.txt', 'r')
from collections import deque

dx =[-1, +1, 0, 0]
dy =[0, 0, -1, +1]


def BFS(s, arrival):
    # print(arrival)
    visit[s[0]][s[1]] = True
    Q = deque()
    Q.append(s)
    D[s[0]][s[1]] = 1
    P[s[0]][s[1]] = 1
    while Q:
        v = Q.popleft()
        repeat = 1

        for w in range(4):
            x = v[0] + dx[w]
            y = v[1] + dy[w]
            # print(x,y)
            if 0 <= x < N and 0 <= y < M:
                # print(x,y)
                if maze[x][y][P[v[0]][v[1]]] == 0 and D[x][y][P[v[0]][v[1]]] > (D[v[0]][v[1]][P[v[0]][v[1]]] + 1):
                    visit[x][y] = True
                    # print([x,y], v, D[x][x])
                    D[x][y] = D[v[0]][v[1]] + 1
                    P[x][y] = P[v[0]][v[1]]
                    Q.append([x, y])
                if D[x][y] > (D[v[0]][v[1]] + 1) and maze[x][y] == 1 and P[v[0]][v[1]] == 1:
                    visit[x][y] = True
                    # print([x,y], v, D[x][x])
                    D[x][y] = D[v[0]][v[1]] + 1
                    P[x][y] = 0
                    Q.append([x, y])
                if x == arrival[0] and y == arrival[1]:
                    print(D[x][y])
                    # print('도착')
                    return

    else:
        if arrival == s:
            print(D[arrival[0]][arrival[1]])
        else:
            print(-1)





start = [0, 0]
N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]
visit = [[False for _ in range(M)] for __ in range(N)]
D = [[[0, 0] for _ in range(M)] for __ in range(N)]
P = [[0 for _ in range(M)] for __ in range(N)]
# print(maze)
BFS(start, [N-1, M-1])
# print(D)
# print(P)