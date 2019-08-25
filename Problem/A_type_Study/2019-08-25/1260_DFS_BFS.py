def DFS(v):
    print(v, end=' ')
    visit[v] = [True]
    for w in G[v]:
        if not visit[w]:
            # print(w, end=' ')
            visit[w] = True
            DFS(w)

def BFS(v):
    Q = deque()
    visit[v] = True; print(v, end =' ')
    Q.append(v)
    while Q:
        s = Q.popleft()
        for w in G[s]:
            if not visit[w]:
                visit[w] = True; print(w, end=' ')
                Q.append(w)

import sys; sys.stdin = open('1260.txt', 'r')
from collections import deque


N, M, V = list(map(int, input().split()))
# print(N,M,V)
G = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
# print(G)
for i in range(M):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)
    G[u].sort()
    G[v].sort()
# print(G)
DFS(V)
print()
visit = [False] * (N + 1)
BFS(V)