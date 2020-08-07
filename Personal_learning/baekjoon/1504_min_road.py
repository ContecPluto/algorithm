import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def BFS(start, end):
    Q = [(0, start)]
    visit = [0xfffff] * (N + 1)
    visit[start] = 0
    while Q:
        y, x = heappop(Q)
        if y > visit[x]:
            continue
        for ny, nx in G[x]:
            ny += y
            if ny < visit[nx]:
                visit[nx] = ny
                heappush(Q, (ny, nx))
    return visit[end]


N, E =  map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

v1, v2 = map(int, input().split())
route_1 = BFS(1, v1) + BFS(v2, N)
route_2 = BFS(1, v2) + BFS(v1, N)

result = min(route_1, route_2) + BFS(v1, v2)
print(-1 if result >= 0xfffff else result)
