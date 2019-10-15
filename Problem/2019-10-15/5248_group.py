import sys; sys.stdin = open('5248.txt','r')

def DFS(s):
    visit[s] = True
    for v in G[s]:
        if visit[v] == False:
            DFS(v)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visit = [False] * (N + 1)
    G = [[] for _ in range(N + 1)]
    cnt = 0
    for i in range(0, len(arr), 2):
        G[arr[i]].append(arr[i+1])
        G[arr[i+1]].append(arr[i])
    # print(G)
    for i in range(1, N+1):
        if visit[i] == False:
            cnt += 1
            DFS(i)
    print('#{} {}'.format(tc, cnt))
