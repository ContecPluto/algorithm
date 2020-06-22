import sys; sys.stdin = open('1006.txt', 'r')

dx = [0, -1, 0]
dy = [1, 0, -1]

def DFS(s, total):
    x, y = s
    visit[x][y] = True
    value = 0
    idx = []
    for z in range(3):
        tx = x + dx[z]
        ty = y + dy[z]
        if -1 <= tx < 2 and -1 <= ty < N:
            if not visit[tx][ty] and value < total + arr[tx][ty] <= W:
                value = total + arr[tx][ty]
                idx = [tx, ty]
    if value:
        visit[idx[0]][idx[1]] = True





for tc in range(int(sys.stdin.readline())):
    N, W = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    visit = [[False] * N for _ in range(2)]
    result = 0
    for a in range(3):
        for i in range(2):
            for j in range(N):
                if visit[i][j]: continue
                DFS([i, j], arr[i][j])
                result += 1
    sys.stdout.write(str(result)+'\n')
