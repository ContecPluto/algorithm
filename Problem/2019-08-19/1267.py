def DFS(s):
    print(s, end =' ')
    for w in G[s]:
        if view[w] == 1:
            view[w] -= 1
            DFS(w)
        elif view[w] >= 2:
            view[w] -= 1

import sys; sys.stdin = open('1267.txt', 'r')

for t in range(1, 11):
    V, E = map(int, input().split())
    number = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]  # 정점번호 1~V
    result = []

    for _ in range(len(number)//2):
        u, v = number.pop(0), number.pop(0)
        G[u].append(v)
        view = [0] * (V + 1)

    for i in range(1, V+1):
        for j in G[i]:
            view[j] += 1

    print('#{}'.format(t), end=' ')
    for i in range(1, len(view)):
        if not view[i]:
            result.append(i)
    # print(result)
    for i in result:
        DFS(i)
    print()




