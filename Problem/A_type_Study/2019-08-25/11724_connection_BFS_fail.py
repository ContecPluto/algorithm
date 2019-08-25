def BFS(v):
    visit[v] = True
    Q = deque()
    Q.append(v)
    while Q:
        s = Q.popleft()
        for w in G[s]:
            if not visit[w] :
                visit[w] = True
                Q.append(w)

import sys; sys.stdin = open('11724.txt', 'r')
from collections import deque


N, M = list(map(int, input().split()))
G = [[] for _ in range(N + 1) ]
visit = [False] * (N + 1)
visit[0] = True
count = 0

for _ in range(M):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    # G[v].append(u)


for i in range(1, N + 1):
    if not visit[i]:
        count += 1
        BFS(i)
    if visit.count(False)==0:
        break

print(count)