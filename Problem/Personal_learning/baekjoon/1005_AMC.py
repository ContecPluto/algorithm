import sys; sys.stdin = open('1005.txt', 'r')
from collections import deque

def BFS():
    result = 0
    Q = deque([[0]])
    while Q:
        y = Q.popleft()
        time = 0
        Q_inner = []
        for x in y:
            for i in G[x]:
                if i == last:
                    return result + arr[last]
                time = max(time, arr[i])
                # for j in P[x]:
                #     if not visit[j]:
                #         break
                # else:
                Q_inner.append(i)
                visit[i] = True
        else:
            result += time
            if Q_inner:
                Q.append(Q_inner)
    return result

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    G = [[] for _ in range(N+1)]
    P = [[] for _ in range(N+1)]
    visit = [False for _ in range(N+1)]
    for i in range(K):
        x, y = map(int, input().split())
        if i == 0:
            G[0].append(x)
        G[x].append(y)
        # P[y].append(x)
    last = int(input())
    print(BFS())
