from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

D = ((0, 1), (0, -1), (-1, 0), (1, 0))

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)] 
visit = [[0xfffff] * M for _ in range(N)]
Q = [[1, 1, 0, 0]]
visit[0][0] = 1

while Q:
    c, w, x, y = heappop(Q)
    c += 1
    for dx, dy in D:
        tx = x + dx
        ty = y + dy
        if 0 <= tx < N and 0 <= ty < M:
            if visit[tx][ty] >= c:
                if maze[tx][ty] == 1 and w == 1:
                    heappush(Q, [c, 0, tx, ty])
                    visit[tx][ty] = c
                elif maze[tx][ty] == 0:
                    heappush(Q, [c, w, tx, ty])
                    visit[tx][ty] = c

result = visit[N-1][M-1]
print(-1 if result >= 0xfffff else result)