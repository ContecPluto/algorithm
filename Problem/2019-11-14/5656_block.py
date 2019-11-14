import sys; sys.stdin = open('5656.txt', 'r')
from copy import deepcopy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def ball(times, total_brick):
    global answer, arr
    if answer == 0:
        return
    if times == N:
        answer = min(answer, total_brick)
        return
    Q = deque()
    previous = deepcopy(arr)
    for width in range(W):
        break_brick = 0
        flag = True
        for high in range(H):
            if arr[high][width]:
                z = arr[high][width] - 1
                if z > 0:
                    Q.append((high,width, z))
                break_brick += 1
                arr[high][width] = 0
                break
        else:
            flag = False
        while Q:
            x, y, z = Q.popleft()
            for i in range(4):
                tx = x
                ty = y
                for cnt in range(z):
                    tx += dx[i]
                    ty += dy[i]
                    if 0 <= tx < H and 0 <= ty < W:
                        if arr[tx][ty]:
                            if arr[tx][ty] != 1:
                                Q.append((tx, ty, arr[tx][ty] - 1))
                            arr[tx][ty] = 0
                            break_brick += 1
        if flag:
            for a in range(H-1, -1, -1):
                for b in range(W):
                    if arr[a][b]: continue
                    for c in range(a-1, -1, -1):
                        if arr[c][b]:
                            arr[c][b], arr[a][b] = arr[a][b], arr[c][b]
                            break
        ball(times+1, total_brick - break_brick)
        arr = deepcopy(previous)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]
    total_brick, answer = W*H, 0xfffffff
    for _ in range(H):
        total_brick -= origin[_].count(0)
    arr = deepcopy(origin)
    ball(0, total_brick)
    print('#{} {}'.format(tc, answer))
