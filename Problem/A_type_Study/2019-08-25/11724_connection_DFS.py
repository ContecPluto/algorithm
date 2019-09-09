def DFS(v):
    # print(v, end=' ')
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            visit[w] = True
            DFS(w)
            
import sys; sys.stdin = open('11724.txt', 'r')
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))
G = [[] for _ in range(N + 1) ]
visit = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)


for i in range(1, N + 1):
    if not visit[i]:
        count += 1
        DFS(i)
print(count)