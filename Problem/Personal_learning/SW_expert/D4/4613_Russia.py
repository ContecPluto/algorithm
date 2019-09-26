import sys; sys.stdin = open('4613.txt','r')


T = int(input())
for tc in range(1, T +1):
    N, M = list(map(int, input().split()))
    flag = [list(input()) for _ in range(N)]
    check = 1000000
    w, b, r = 0,0,0


    for i in range(0, N-2):
        w += M - flag[i].count('W')
        if w > check: break
        for j in range(i+1, N-1):
            b += M - flag[j].count('B')
            if (w+b) > check: break
            for k in range(j+1, N):
                r += M - flag[k].count('R')
            check = min(check, w+b+r)
            r = 0
        b = 0
    print('#{} {}'.format(tc, check))







