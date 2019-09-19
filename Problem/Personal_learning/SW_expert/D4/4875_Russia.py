import sys; sys.stdin = open('4875.txt','r')

T = int(input())
color = ['W', 'B', 'R']
for tc in range(T):
    index = 0
    N, M = list(map(int, input().split()))
    flag = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        if index != 2:
            if flag.count(color[index]) <= flag.count(color[index+1]):
                index += 1
        if i == 0:
            index = 0
        elif i == (N-1):
            index = 2

        for x in range(M):
            if flag[i][x] != color[index]:
                count += 1
    print(count)









