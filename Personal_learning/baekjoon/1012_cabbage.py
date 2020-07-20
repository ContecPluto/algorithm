import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def DFS(position):
    x, y = position
    arr[x][y] = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < M and 0 <= ty < N:
            if arr[tx][ty] == 0: continue
            DFS([tx, ty])

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split(" "))
    arr = [[0]*N for _ in range(M)]
    posi = []
    for i in range(K):
        x, y =  map(int, input().split(" "))
        arr[x][y] += 1
        posi.append([x, y])

    cnt = 0
    for x, y in posi:
        if arr[x][y] == 0: continue
        DFS([x, y])
        cnt += 1
    
    result.append(str(cnt) + "\n")
print(*result, end="", sep="")

