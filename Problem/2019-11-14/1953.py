import sys; sys.stdin = open('1953.txt', 'r')


dx = [[], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
dy = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]


def DFS(s, L):
    global answer
    x, y = s
    answer.add((x,y))
    if L == 1:
        return
    cx = dx[arr[x][y]]
    cy = dy[arr[x][y]]
    for i in range(len(cx)):
        tx = x + cx[i]
        ty = y + cy[i]
        if 0 <= tx < N and 0 <= ty < M:
            if not visit[tx][ty]:
                c_x = dx[arr[tx][ty]]
                c_y = dy[arr[tx][ty]]
                if (cx[i] and cx[i] * -1 in c_x) or (cy[i] and cy[i] * -1 in c_y):
                    visit[tx][ty] = True
                    DFS([tx, ty], L - 1)
                    visit[tx][ty] = False


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    answer = set()
    visit = [[False] * M for _ in range(N)]
    DFS([R, C], L)
    print('#{} {}'.format(tc, len(answer)))

