from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def hole_check(ax, ay):
    for adx, ady in D:
        tax = ax + adx
        tay = ay + ady
        if 0 <= tax < N and 0 <= tay < M and chess[tax][tay] == -1:
            air_check(ax, ay)
            break

def air_check(ai, aj):
    chess[ai][aj] = -1
    air_index = [[ai, aj]]
    while air_index:
        ax, ay = heappop(air_index)
        for adx, ady in D:
            tax = ax + adx
            tay = ay + ady
            if 0 <= tax < N and 0 <= tay < M and chess[tax][tay] == 0:
                chess[tax][tay] = -1
                heappush(air_index, [tax, tay])

D = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]
index = [(i, j) for i in range(N) for j in range(M) if chess[i][j] == 1]
cnt = len(index)
result = 0
air_check(0, 0)
while index:
    air = []
    in_chess = []
    is_hole = []
    while index:
        x, y = heappop(index)
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
        hole_check(i, j)
    index = in_chess[::]

    if len(in_chess):
        cnt = len(in_chess)
    result += 1

print(result)
print(cnt)