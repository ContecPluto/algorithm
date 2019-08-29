import sys; sys.stdin = open('1238.txt', 'r')
from collections import deque

def BFS(s):
    Q = deque()
    D[s] = 1
    P[s] = s
    visit[s] = True#; print(s, end=' ')
    Q.append(s)
    while Q:
        v = Q.popleft()   #pop은 오른쪽, popleft는 왼쪽
        for w in G[v]:
            if not visit[w]:
                visit[w] = True#; print(w, end=' ')
                D[w] = D[v] + 1
                Q.append(w)




for tc in range(1, 11):
    result = []
    V, E = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    visit = [False for _ in range(101)]
    D = [0 for _ in range(101)]
    P = [[] for _ in range(101)]

    for i in range(0, V, 2):
        u = nums[i]
        v = nums[i+1]
        G[u].append(v)
    BFS(E)
    max_result = max(D)
    for i in range(len(D)):
        if D[i] == max_result:
            result.append(i)
    print('#{} {}'.format(tc, max(result)))





