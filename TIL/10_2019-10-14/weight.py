from collections import deque

def BFS(s):
    D[s] = 0 #출발점의 D값을 0으로 설정
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.append(v)
import sys
sys.stdin = open("weighted_graph.txt", "r")
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
P = [i for i in range(V + 1)]
Idx = [i for i in range(V + 1)]
D = [0xfffff] * (V + 1)  # D[] 배열 초기값 설정
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
BFS(1)
print(Idx[1:])
print(D[1:])
print(P[1:])
