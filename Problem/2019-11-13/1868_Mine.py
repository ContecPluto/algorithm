import sys; sys.stdin = open('1868.txt','r')

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def mine_check(s):
    x, y = s
    if arr[x][y] == '*': return
    visit[x][y] = True
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if arr[tx][ty] == '*':
                break
    else:
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if arr[tx][ty] == '.' and visit[tx][ty] == False:
                    mine_check([tx, ty])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    answer = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == '*':
                visit[x][y] = True
                continue
            for i in range(8):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < N and 0 <= ty < N:
                    if arr[tx][ty] == '*':
                        break
            else:
                if visit[x][y] == False:
                    visit[x][y] = True
                    answer += 1
                    mine_check([x, y])
    for i in range(N):
        answer += visit[i].count(False)
    print('#{} {}'.format(tc, answer))