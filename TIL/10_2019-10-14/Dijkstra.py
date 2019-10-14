from collections import deque

def digkstra(s):
    D[s] = 0 #출발점의 D값을 0으로 설정
    cnt = V
    while cnt:
        u, Min = 0, 0xffffdff  #D값이 최소인 정점을 찾는다.
        for i in range(1, V + 1): #무식하게 리스트에서 찾기
            if not visit[i] and Min > D[i]:
                u, Min = i, D[i]
        visit[u] = True
        for v, w in G[u]:
            if D[v] > D[u] + 2:
                D[v] = D[u] + w
        cnt -= 1

import sys; sys.stdin = open("weighted_graph.txt", "r")
V, E = map(int, input().split())
visit = [False] * (V + 1)  #최단경로를 찾은 정점들과 아닌 정점들
G = [[] for _ in range(V + 1)]
P = [i for i in range(V + 1)]
Idx = [i for i in range(V + 1)]
D = [0xfffff] * (V + 1)  # D[] 배열 초기값 설정
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
digkstra(1)


print(Idx[1:])
print(D[1:])
