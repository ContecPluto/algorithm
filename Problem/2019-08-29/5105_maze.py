import sys; sys.stdin = open('5105.txt','r')
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def DFS(x, y):
    # print('좌표', x, y, end=' ')
    visit[x][y] = True
    for j in range(4):
        tx = x + dx[j]
        ty = y + dy[j]
        if 0 <= tx <= (N-1) and 0 <= ty <= (N-1) and visit[tx][ty] == False:
            # print(visit[tx][ty] == False, maze[tx][ty])
            if maze[tx][ty] == 3:
                cnt[tx][ty] = cnt[x][y]
                result = 1
            if maze[tx][ty] == 0:
                # print('시작')
                cnt[tx][ty] = cnt[x][y] + 1
                # print(x,y ,tx, ty)
                # print(cnt)
                DFS(tx, ty)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [[0 for _ in range(N)] for __ in range(N)]
    maze = [list(map(int, input())) for _ in range(N)]
    visit = [[False for _ in range(N)] for __ in range(N)]
    result = 0
    check = [0]

    for i in range(len(maze)):
        if maze[i].count(3) == 1:
            a = i
            b = maze[i].index(3)

        if maze[i].count(2) == 1:
            # print(i, maze[i].index(2))
            DFS(i, maze[i].index(2))
            # break
    # print(cnt)
    print('#{} {}'.format(tc, cnt[a][b]))
