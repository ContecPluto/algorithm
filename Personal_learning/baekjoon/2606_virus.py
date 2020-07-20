from collections import deque

N = int(input()) + 1
t = int(input())
G = [[] for _ in range(N)]
visit = [False] * N
visit[1] = True

arr = set()
arr.add(1)
for t in range(t):
    s, p = map(int, input().split(" "))
    G[s].append(p)
    G[p].append(s)

Q = deque()
Q.append(1)
while Q:
    x = Q.popleft()
    for i in G[x]:
        if visit[i]: continue
        Q.append(i)
        visit[i] = True
print(sum(visit) - 1)