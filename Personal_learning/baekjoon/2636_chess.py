from sys import stdin
from collections import deque
input = stdin.readline

def air(ai, aj):
    air_index = deque([ai, aj])
    while air_index:
        ax, ay = air_index.popleft()
        for adx, ady in D:
            tax = ax + adx
            tay = ay + ady
            if 0 <= tx < M and 0 <= ty < N and chess[tx][ty] == 0:
                chess[x][y] = -1

D = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]
index = [[i, j]  for i in range(N) for j in range(M) if chess[i][j] == 1]
index = deque(index)
cnt = 0
air(0, 0)
hole_idx = [[i, j]  for i in range(N) for j in range(M) if chess[i][j] == 0]



while index:
    air = []
    in_chess = []
    while index:
        x, y = index.popleft()
        is_air = False
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < M and 0 <= ty < N and chess[tx][ty] == -1:
                is_air = True
                break
        if is_air:
            air.append([x, y])
        else:
            in_chess.append([x, y])

    for i, j in air:
        chess[i][j] = 0

    index = deque(in_chess)
    if len(in_chess):
        cnt = len(in_chess)
    print(*chess, sep="\n")
    print()
print(cnt)
