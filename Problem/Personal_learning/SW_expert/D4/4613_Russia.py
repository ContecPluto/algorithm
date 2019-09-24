import sys; sys.stdin = open('4613.txt','r')


T = int(input())
color = ['W', 'B', 'R']
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    flag = [list(input()) for _ in range(N)]
    check = []
    flag_color = ['B' for _ in range(N)]
    flag_color[0] = 'W'
    flag_color[-1] = 'R'




    print('#{} {}'.format(tc, min(check)))







