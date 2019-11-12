import sys; sys.stdin = open('1949.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(s, n, l):
    global length
    x, y = s
    visit[x][y] = True
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if arr[tx][ty] < arr[x][y] and visit[tx][ty] == False:
                DFS([tx, ty], n, l+1)
            elif n == 1 and visit[tx][ty] == False:
                for _ in range(K):
                    arr[tx][ty] -= 1
                    if arr[x][y] > arr[tx][ty]:
                        DFS([tx, ty], n - 1, l + 1)
                arr[tx][ty] += K
    visit[x][y] = False
    length = max(l, length)


T = int(input())
for tc in range(1, T+1):
    length = 0
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    max_value = max([max(i) for i in arr])
    for x in range(N):
        for y in range(N):
            if arr[x][y] == max_value:
                DFS([x, y], 1, 1)
    print('#{} {}'.format(tc, length))


