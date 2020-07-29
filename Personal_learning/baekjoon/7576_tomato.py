from collections import deque
from sys import stdin
input = stdin.readline

D = ((0, -1), (0, 1), (1, 0), (-1, 0))

tomatos = []
Q = deque()
N, M = map(int, input().split())

for i in range(M):
    line = list(map(int, input().split()))
    tomatos.append(line)
    Q += [[i, j, -1] for j in range(N) if line[j] == 1]

while Q:
    x, y, z = Q.popleft()
    z += 1
    for dx, dy in D:
        tx = x + dx
        ty = y + dy
        if 0 <= tx < M and 0 <= ty < N and tomatos[tx][ty] == 0:
            tomatos[tx][ty] = 1
            Q.append([tx, ty, z])

for tomato in tomatos:
    if tomato.count(0) != 0:
        print(-1)
        break
else:
    print(z)