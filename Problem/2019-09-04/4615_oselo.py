import sys; sys.stdin = open('4615.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    oselo = [[0 for _ in range(N)] for __ in range(N)]
    count = [0 for _ in range(3)]

    # 판 세팅 흑돌 : 1, 백돌 : 2
    c = N//2
    oselo[c][c] = 2
    oselo[c-1][c-1] = 2
    oselo[c][c-1] = 1
    oselo[c-1][c] = 1

    for turn in range(M):
        x, y, c = list(map(int, input().split()))
        x, y = x-1, y-1
        oselo[x][y] = c
        # print('시작', x,y,c)
        # for i in range(N):
        #     print(oselo[i])
        # print()

        # #우측
        # for i in range(y, N):
        #     if i==y: continue
        #     if oselo[x][i] == c:
        #         # print('우측', x,i,c)
        #         # print(y)
        #         for j in range(y, i):
        #             # print(x,j)
        #             oselo[x][j] = c
        #         break
        #     elif oselo[x][i] == 0:
        #         break
        #
        # #좌측
        # for i in range(y, -1, -1):
        #     if i==y: continue
        #     if oselo[x][i] == c:
        #         # print('좌측')
        #         for j in range(y, i, -1):
        #             oselo[x][j] = c
        #         break
        #     elif oselo[x][i] == 0:
        #         break
        #
        #
        # #위
        # for i in range(x, -1, -1):
        #     if i== x : continue
        #     # print('위')
        #     if oselo[i][y] == c:
        #         # print(x, y, oselo[i][y])
        #         for j in range(x, i, -1):
        #             # print(j,y)
        #             oselo[j][y] = c
        #         break
        #     elif oselo[i][y] == 0:
        #         break
        # #아래
        # for i in range(x, N):
        #     if i== x : continue
        #     # print('아래',i, y, c)
        #     if oselo[i][y] == c:
        #         # print('change',i, y)
        #         for j in range(x, i):
        #             oselo[j][y] = c
        #         break
        #     elif oselo[i][y] == 0:
        #         break
        #대각선

        dx = [-1, -1, +1, +1, -1, 1, 0, 0]
        dy = [+1, -1, -1, +1, 0, 0, -1, 1]
        for k in range(8):
            idx_x, idx_y = x + dx[k], y + dy[k]
            ch_x, ch_y = 10000, 100000
            while True:
                # print(idx_x, idx_y)
                if idx_x < 0 or idx_y > N - 1 or idx_y < 0 or idx_x > N - 1:
                    break
                if oselo[idx_x][idx_y] == c:
                    ch_x, ch_y = x + dx[k], y + dy[k]
                    while True:
                        if ch_x == idx_x and ch_y == idx_y:
                            break
                        oselo[ch_x][ch_y] = c
                        ch_x += dx[k]
                        ch_y += dy[k]

                elif oselo[idx_x][idx_y] == 0:
                    break
                if ch_x == idx_x and ch_y == idx_y:
                    break
                idx_x += dx[k]
                idx_y += dy[k]

    for x in range(N):
        for y in range(N):
            count[oselo[x][y]] += 1
    print('#{} {} {}'.format(tc, count[1], count[2]))

