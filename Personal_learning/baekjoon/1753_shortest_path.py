# from collections import deque
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = 0xffffff

V, E = map(int, input().split())
start = int(input())
visit = [INF] * (V+1)
visit[start] = 0
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v])

Q = []
heappush(Q, [0, start])
while Q:
    x, y = heappop(Q)
    for p, s in G[y]:
        p += x
        if p < visit[s]:
            visit[s] = p
            heappush(Q, [p, s])

for i in range(1, V+1):
    if visit[i] == INF:
        print("INF")
    else:
        print(visit[i])