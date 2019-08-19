def DFS(v):
    visit[v] = True; print(v, end=' ')
    print(G[v])
    for w in G[v]:
        print(G[v], w, visit[w])
        if not visit[w]:
            DFS(w)

import  sys
sys.stdin = open('DFS.txt', 'r')


V, E = map(int, input().split())  #정점수, 간선수
G = [[] for _ in range(V+1)]  #정점번호 1~V

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# for i in range(1, V+1):
#     print(i, '-->', G[i])

S = []
visit = [False] * (v + 1)

DFS(1)



# def DFS(v):  #시작점
#     S = []
#     visit = [False] * (v + 1)
#     시작점을 방문한다.
#     visit[v] = True
#
#     S.append(v)  #시작점을 스택에 push
#     while S:        #빈스택이 아닐동안
#         # v의 방문하지 않은 인접접점을 찾는다. ==> w
#         for w in G[v]:
#             if not visit[w]:
#                 visit[w] = True #w를 방문하고
#                 S.append(v)
#                 v = w      #w를 현재 방문하는 정점으로 설정
#                 break
#         else:
    #         v = S.pop()

