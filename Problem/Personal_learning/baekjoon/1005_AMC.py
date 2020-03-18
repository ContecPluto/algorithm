import sys; sys.stdin = open('1005.txt', 'r')
from collections import deque

def BFS():
    global time
    Q = deque([start for start in range(1, N)])
    while Q:
        x = Q.popleft()
        for i in G[x]:
            if time[x] + arr[i] > time[i]:
                time[i] = time[x] + arr[i]
                Q.append(i)
    return str(time[last])


T = int(sys.stdin.readline())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    N += 1
    arr = list(map(int, sys.stdin.readline().split()))
    arr.insert(0, 0)
    G = [[] for _ in range(N)]
    time = arr[::]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        G[x].append(y)
    last = int(sys.stdin.readline())
    sys.stdout.write(BFS() + '\n')
