import sys; sys.stdin = open('mst_input.txt', 'r')



V, E = map(int, input().split())
G = [[] for  _ in range(V)]  #0~ V-1
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

    key = [0xfffff] * V
    key[0] = 0
    pi = [-1] * V  # - 1=> NULL 없다
    visit = [False] *  V
    cnt = V
    while cnt:
        # key값이 최소인 정점을 찾는다.
        u, Min = 0, 0xffffff
        for i in range(V):
            if not visit[i] and Min > key[i]:
                u, Min = i, key[i]
        visit[u] = True
        # u의 인접정점을 찾아서 key, pi를  변경
        for v, w in G[u]:
            if w < key[v]:
                key[v] = w
                pi[v] = u
        # print(cnt)
        cnt -= 1
    print(pi)