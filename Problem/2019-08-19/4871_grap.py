def DFS(s, g):
    visit[s] = True
    # print(s, end=' ')
    # print(G[s])
    global result
    if s == g:
        result = 1
    else:
        for w in G[s]:
            # print(G[s], w, visit[w])
            if not visit[w]:
                DFS(w, g)


import sys
sys.stdin = open('4871.txt', 'r')

T = int(input())

for num in range(1, T+1):
    result = 0
    V, E = map(int, input().split())  # 정점수, 간선수
    G = [[] for _ in range(V + 1)]  # 정점번호 1~V

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)

    visit = [False] * (V + 1)

    s, g = map(int, input().split())
    DFS(s, g)

    print('#{} {}'.format(num, result))
