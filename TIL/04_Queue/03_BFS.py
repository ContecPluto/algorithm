def BFS(v):
    visit[v] = True
    Q = []
    D = [v]
    print(v, end=' ')
    Q.append(v)
    while Q:
        s = Q.pop(0)
        for i in G[s]:
            if visit[i] == False:
                print(i, end=' ')
                visit[i] = True
                Q.append(i)
                D.append(i)
    print()




adj_list = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
G = [[] for _ in range(8)]
visit = [False] * 8
print(visit)

for u, v in adj_list:
    G[u].append(v)
print(G)
BFS(1)

