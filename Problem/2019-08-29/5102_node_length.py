import sys; sys.stdin =open('5102.txt', 'r')
from collections import deque

def BFS(s) : #s:시작점
    #큐를 생성
    #시작점을 방문하고, 큐에 삽입

    #빈 큐가 인동안
        #v: 큐에 정점을 하나 꺼내온다
        #v의 방문하지 안은 인접 정점 w를 찾는다
            #w를 방문하고 큐에 삽입
    Q = deque()
    D[s] = 0
    P[s] = s
    visit[s] = True
    Q.append(s)
    while Q:
        v = Q.popleft()   #pop은 오른쪽, popleft는 왼쪽

        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    D = [[0] for _ in range(V + 1)]
    P = [[] for _ in range(V + 1)]
    visit = [False] * ( V + 1 )
    start, end = list(map(int, input().split()))
    # print(start,end)
    BFS(start)
    print('#{} {}'.format(tc, D[end]))

    # print()
    # print(D)
    # print(P)

