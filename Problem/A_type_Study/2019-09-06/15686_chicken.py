import sys; sys.stdin = open('15686.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(v):
    global HNC
    HNC = [[],[]]
    Q = deque()
    Q.append(v)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if not visit[tx][ty]:
                    Q.append([tx, ty])
                    visit[tx][ty] = True
                    if chicken[tx][ty] == 1:
                        # print('가정집', tx, ty)
                        HNC[0].append([tx, ty])
                    elif chicken[tx][ty] == 2:
                        # print('치킨집', tx, ty)
                        HNC[1].append([tx, ty])

def backtrack(k, start):
    global result
    if k == R:
        # print(choice)
        # print(choice)
        check = 0
        for j in HNC[0]:
            total = 1000000
            for i in choice:
                # print('치킨집',j,'가정집', i, abs(j[0]-i[0])+abs(j[1]-i[1]))
                if total > (abs(j[0]-i[0])+abs(j[1]-i[1])):
                    total = (abs(j[0]-i[0])+abs(j[1]-i[1]))
            check += total
            # print(total)
        # print(check, choice)
        result = min(result, check)

    else:
        for i in range(start, N):
            choice[k] = HNC[1][i]
            backtrack(k + 1, i + 1)





N, M = list(map(int, input().split()))
chicken = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for __ in range(N)]
count = [100000 for _ in range(2 * N)]
result = 1000000
BFS([0, 0])
N = len(HNC[1])
R = M
choice = ['']*R
backtrack(0,0)
print(result)

