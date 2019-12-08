import sys; sys.stdin = open('17822.txt', 'r')
from collections import deque

def DFS(s, ori):
    global change
    x_idx, y_idx = s
    for k in range(4):
        tx = x_idx + dx[k]
        ty = y_idx + dy[k]
        if 0 <= tx < N:
            if ty >= M: ty = 0
            elif ty == -1: ty = M-1
            if arr[tx][ty] == ori:
                if arr[i][j] != 0:
                    arr[i][j] = 0
                change += 1
                arr[tx][ty] = 0
                DFS([tx, ty], ori)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N, M, T = map(int, input().split())
arr = deque(deque(map(int, input().split())) for _ in range(N))
spin = [list(map(int, input().split())) for _ in range(T)]
total = 0

for a in spin:
    change = 0
    for b in range(a[0], N+1, a[0]):
        b -= 1
        if a[1] == 0:
            arr[b].rotate(a[2])
        else:
            arr[b].rotate(-a[2])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            DFS([i, j], arr[i][j])
    if change == 0:
        avg = []
        for c in arr:
            for d in c:
                if d == 0: continue
                avg.append(d)
        if len(avg) == 0:
            break
        avg = sum(avg)/len(avg)
        for e in range(N):
            for f in range(M):
                if arr[e][f] == 0: continue
                if arr[e][f] > avg:
                    arr[e][f] -= 1
                elif arr[e][f] < avg:
                    arr[e][f] += 1
for sum_total in arr:
    total += sum(sum_total)
print(total)



