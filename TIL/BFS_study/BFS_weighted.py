def BFS(s): #s:시작점
    #큐를 생성
    #시작점을 방문하고, 큐에 삽입

    #빈 큐가 인동안
        #v: 큐에 정점을 하나 꺼내온다
        #v의 방문하지 안은 인접 정점 w를 찾는다
            #w를 방문하고 큐에 삽입
    Q = deque()
    D[s] = 0
    print(s, end=' ')
    Q.append(s)

    while Q:
        u = Q.popleft()   #pop은 오른쪽, popleft는 왼쪽
        for v, w in G[u]:
            if D[v] > ( D[u] + w ):
                D[v] = D[u] + w
                P[v] = u
                Q.append(v)
    print()



import sys
from collections import deque
sys.stdin = open("weighted_graph.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
W = [[[] for _ in range(V + 1)] for __ in range(V + 1)]
total = 0

for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

D = [0xfffff] * (V + 1)
P = [[] for _ in range(V + 1)]
visit = [100000] * ( V + 1 )
BFS(1)
# print()
#
# print(W)
# print(D)
# print(P)
print(D)

