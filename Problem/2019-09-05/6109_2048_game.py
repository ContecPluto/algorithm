import sys;sys.stdin = open('6109.txt', 'r')

directions = {'up':0, 'down':1, 'right':2, 'left':3}
dx = [-1, +1, 0, 0]
dy = [0, 0, +1, -1]

T = int(input())
for tc in range(1, T+1):
    N, direction = list(input().split())
    N = int(N)
    game = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False for _ in range(N)] for __ in range(N)]
    ix = dx[directions[direction]]
    iy = dy[directions[direction]]

    if direction == 'up' or direction == 'left':
        for x in range(N):
            for y in range(N):
                tx, ty = x + ix, y + iy
                cx, cy = x, y
                if game[x][y]:
                    while 0 <= tx < N and 0 <= ty < N:
                        if game[cx][cy] == game[tx][ty] and (visit[tx][ty] == False and visit[cx][cy] == False):
                            game[tx][ty], game[cx][cy] = game[cx][cy] * 2, 0
                            visit[tx][ty] = True
                        if game[tx][ty] == 0 and game[cx][cy]:
                            game[tx][ty], game[cx][cy] = game[cx][cy] + 0, 0
                        if visit[tx][ty]:
                            break
                        cx += ix
                        cy += iy
                        tx += ix
                        ty += iy


    if direction == 'down' or direction == 'right':
        for x in range(N-1, -1, -1):
            for y in range(N-1, -1, -1):
                tx, ty = x + ix, y + iy
                cx, cy = x, y
                if game[x][y]:
                    while 0 <= tx < N and 0 <= ty < N:
                        if game[cx][cy] == game[tx][ty] and (visit[tx][ty] == False and visit[cx][cy] == False):
                            game[tx][ty], game[cx][cy] = game[cx][cy] * 2, 0
                            visit[tx][ty] = True
                        if game[tx][ty] == 0:
                            game[tx][ty], game[cx][cy] = game[cx][cy] + 0, 0
                        if visit[tx][ty]:
                            break
                        cx += ix
                        cy += iy
                        tx += ix
                        ty += iy

    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, game[i])))



