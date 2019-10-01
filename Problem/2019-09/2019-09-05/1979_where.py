import sys; sys.stdin = open('1979.txt', 'r')

T = int(input())
dx = [+1, 0]
dy = [0, +1]

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    M_count = 0

    #오른쪽 & 아래
    for x in range(N):
        for y in range(N):
            if puzzle[x][y] == 1:
                for z in range(2):
                    cnt = 1
                    tx = x + dx[z]
                    ty = y + dy[z]
                    ctx = x - dx[z]
                    cty = y - dy[z]

                    if 0 <= ctx < N and 0 <= cty < N:
                        if puzzle[ctx][cty] == 1:
                            continue
                    # print('시작',x,y)
                    while True:
                        if tx >= N or ty >= N:
                            break
                        # print(tx, ty)
                        if puzzle[tx][ty] == 1:
                            # print(tx,ty)
                            cnt += 1
                        else:
                            break
                        tx += dx[z]
                        ty += dy[z]

                    if cnt == M:
                        # print(x,y)
                        M_count += 1

    print('#{} {}'.format(tc, M_count))

