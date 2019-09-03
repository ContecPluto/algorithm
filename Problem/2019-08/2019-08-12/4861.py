import sys
sys.stdin = open('4861.txt','r')

T =int(input())
for num in range(1, T+1):
    # print('시작')
    N, M = list(map(int,input().split()))
    words = [input() for _ in range(N)]

    for x in range(N):
        for y in range(N-M+1):
            x_cheak, y_cheak = '', ''
            for z in range(y, y+M):
                x_cheak += words[x][z]
                y_cheak += words[z][x]
                # print(x_cheak, y_cheak)
            if x_cheak == x_cheak[::-1] and x_cheak:
                # print('x회문')
                print('#{} {}'.format(num, x_cheak))
            if y_cheak == y_cheak[::-1] and y_cheak:
                # print('y회문')
                print('#{} {}'.format(num, y_cheak))

    
