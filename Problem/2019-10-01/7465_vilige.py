import sys;sys.stdin = open('7465.txt', 'r')

def DFS(s):
    visit[s] = True
    for u in G[s]:
        if visit[u] == False:
            DFS(u)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [False for _ in range(N + 1)]
    cnt = 0
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    for i in range(1, N+1):
        if visit[i] == False:
            cnt += 1
            DFS(i)
    print('#{} {}'.format(tc, cnt))