import sys; sys.stdin = open('5521.txt','r')
from collections import deque
# def BFS(s):


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    D = [0xffffff] * (N + 1)
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    D[1] = 0
    Q = deque()
    Q.append(1)
    cnt = 0
    while Q:
        t = Q.popleft()
        if D[t] > 1: continue
        for v in G[t]:
            if D[v] > D[t] + 1:
                Q.append(v)
                D[v] = D[t] + 1
                cnt += 1
    print('#{} {}'.format(tc, cnt))


