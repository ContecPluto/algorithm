from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

N = int(input())
G = [[] for _ in range(N + 1)]
visit = [0xffffffff] * (N+1)
M = int(input())
for m in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))
start, end = map(int, input().split())

Q = [(0, start)]
while Q:
    x, y = heappop(Q)
    for u, v in G[y]:
        u += x
        if visit[v] > u:
            visit[v] = u
            heappush(Q, (u, v))
print(visit[end])