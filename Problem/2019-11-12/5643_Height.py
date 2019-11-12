import sys; sys.stdin = open('5643.txt', 'r')
from collections import deque
def BFS(x, t):
    ans = 0
    Q = deque()
    Q.append(x)
    while Q:
        s = Q.popleft()
        for a in G[t][s]:
            if visit[a]: continue
            visit[a] = True
            Q.append(a)
            ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    G = [[[] for _ in range(N + 1)], [[] for _ in range(N + 1)]]
    for i in range(M):
        u, v = map(int, input().split())
        G[0][v].append(u)
        G[1][u].append(v)
    cnt = 0

    for j in range(N+1):
        visit = [False] * (N+1)
        if BFS(j, 0) + BFS(j, 1) + 1 == N:
            cnt += 1
    print('#{} {}'.format(tc, cnt))

