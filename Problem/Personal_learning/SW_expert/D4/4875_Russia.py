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

    for i in range(N):
        for j in range(M):
            if flag[i][j] != flag_color[i]:
                flag[i][j] = flag_color[i]


