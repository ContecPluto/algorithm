import sys; sys.stdin = open('4875.txt','r')

T = int(input())
color = ['W', 'B', 'R']
for tc in range(1, T+1):
    index = 0
    N, M = list(map(int, input().split()))
    flag = [list(input()) for _ in range(N)]
    check = []
    flag_color = ['B' for _ in range(N)]
    flag_color[0] = 'W'
    flag_color[-1] = 'R'
    print(flag_color)
    for x in range(1, N-1):
        midle = []
        for i in range(2):
            for y in range(N):
                # print(N, flag[y].count(flag_color[y]))
                midle.append(M-flag[y].count(flag_color[y]))
            if flag_color[x - 1] != flag_color[x]:
                flag_color[x] = flag_color[x-1]
            if flag_color[N - x] != flag_color[N - x -1]:

        print(midle)
        check.append(sum(midle))
    print(check)

