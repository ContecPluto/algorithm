from sys import stdin
from heapq import heappop, heappush
from collections import deque
input = stdin.readline

def melt(icebergs):
    ice_index = deque([icebergs[0]])
    visit = {}
    visit[icebergs[0]] = True
    while ice_index:
        ix, iy = ice_index.popleft()
        for idx, idy in D:
            itx, ity = ix + idx, iy + idy
            if 0 < itx < N and 0 < ity < M and see[itx][ity] and visit.get((itx, ity)) != True:
                visit[(itx, ity)] = True
                ice_index.append((itx, ity))
    if len(visit) != len(icebergs):
        return True
    return False
            
D = ((0, -1), (0, 1), (1, 0), (-1, 0))
N, M = map(int, input().split())
see = [list(map(int, input().split())) for _ in range(N)]
ice = deque([(i, j) for i in range(1, N-1) for j in range(1, M-1) if see[i][j]])
result = 0

while ice:
    if melt(ice):
        break

    next_ice = []
    cnt_ice = []
    while ice:
        x, y = ice.popleft()
        # x, y = heappop(ice)
        cnt = 0
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < N and 0 <= ty < M and see[tx][ty] == 0:
                cnt += 1
        else:
            val = see[x][y] - cnt
            cnt_ice.append((x, y, max(val, 0)))
            if val > 0:
                # heappush(next_ice,(x, y))
                next_ice.append((x, y))

    for x, y, cnt in cnt_ice:
        see[x][y] = cnt

    ice = deque(next_ice)
    result += 1
else:
    result = 0
print(result)
