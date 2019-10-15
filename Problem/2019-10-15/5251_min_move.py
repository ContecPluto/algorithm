import sys;sys.stdin = open('5251.txt', 'r')

def DFS(s):
    for v, w in G[s]:
        cost = cnt[s] + w
        if cnt[v] > cost:
            cnt[v] = cost
        else:
            continue
        DFS(v)

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    cnt = [0xffff for _ in range(N + 1)]
    cnt[0] = 0
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    DFS(0)
    print('#{} {}'.format(tc, cnt[N]))
