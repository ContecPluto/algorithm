import sys; sys.stdin = open('4615.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # N=8
    oselo = [[0 for _ in range(N)] for __ in range(N)]
    count = [0 for _ in range(3)]


    # 판 세팅 흑돌 : 1, 백돌 : 2
    c = N//2
    oselo[c][c] = 2
    oselo[c-1][c-1] = 2
    oselo[c][c-1] = 1
    oselo[c-1][c] = 1



    for turn in range(M):
        x,y,c = list(map(int, input().split()))
        x, y = x-1, y-1
        oselo[x][y] = c

        dx = [-1, -1, +1, +1, -1, 1, 0, 0]
        dy = [+1, -1, -1, +1, 0, 0, -1, 1]
        for k in range(8):
            j = 1
            i = 1
            ch_x, ch_y = 100000, 100000
            while True:
                idx_x, idx_y = x+(dx[k]*i), y + (dy[k]*i)
                # print(idx_x, idx_y)
                if idx_x < 0 or idx_y > N - 1 or idx_y < 0 or idx_x > N - 1:
                    break
                if oselo[idx_x][idx_y] == c:
                    # print(idx_x,idx_y,'x,y',x,y)
                    while True:
                        # print(j)
                        ch_x, ch_y =x+(dx[k]*j), y + (dy[k]*j)
                        oselo[ch_x][ch_y] = c
                        if ch_x == idx_x and ch_y == idx_y:
                            break
                        # print('바꿈',ch_x, ch_y,j)
                        j += 1
                elif oselo[idx_x][idx_y] == 0:
                    break
                if ch_x == idx_x and ch_y == idx_y:
                    break
                i += 1

    for x in range(N):
        for y in range(N):
            count[oselo[x][y]] += 1
    print('#{} {} {}'.format(tc, count[1], count[2]))

