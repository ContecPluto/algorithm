import sys; sys.stdin = open('5521.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    Q = [1]
    cnt = {1}
    for t in Q:
        for v in G[t]:
            cnt.add(v)
            if t == 1:
                Q.append(v)
    print('#{} {}'.format(tc, len(cnt)-1))


