from sys import stdin
from collections import deque
input = stdin.readline

def hole_check(ax, ay):
    for adx, ady in D:
        tax = ax + adx
        tay = ay + ady
        if 0 <= tax < N and 0 <= tay < M and chess[tax][tay] == -1:
            air_check(tax, tay)
            break

def air_check(ai, aj):
    air_index = deque([[ai, aj]])
    while air_index:
        ax, ay = air_index.popleft()
        for adx, ady in D:
            tax = ax + adx
            tay = ay + ady
            if 0 <= tax < N and 0 <= tay < M and chess[tax][tay] == 0:
                chess[tax][tay] = -1
                air_index.append([tax, tay])

D = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]
index = [[i, j] for i in range(N) for j in range(M) if chess[i][j] == 1]
index = deque(index)
cnt = len(index)
result = 0
air_check(0, 0)
while index:
    air = []
    in_chess = []
    is_hole = []
    while index:
        x, y = index.popleft()
        is_air = False
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < N and 0 <= ty < M:
                if chess[tx][ty] == -1:
                    is_air = True
                elif chess[tx][ty] == 0:
                    is_hole.append([tx, ty])

        if is_air:
            air.append([x, y])
        else:
            in_chess.append([x, y])

    for i, j in air:
        chess[i][j] = 0
        is_hole.append([i, j])

    for i, j in is_hole:
        air_check(i, j)
    index = deque(in_chess)

    if len(in_chess):
        cnt = len(in_chess)
    result += 1

    # print(*chess, sep="\n", end="\n\n")
    
print(result)
print(cnt)