import sys
sys.stdin = open('1215.txt','r')

for num in range(1, 11):
    # print('시작')
    N = int(input())
    words = [input() for _ in range(8)]
    result = 0

    for x in range(8):
        for y in range(8-N+1):
            x_cheak, y_cheak = '', ''
            for z in range(y, y+N):
                x_cheak += words[x][z]
                y_cheak += words[z][x]
                # print(x_cheak, y_cheak)

            for i in range(len(x_cheak)//2):
                if x_cheak[i] != x_cheak[len(x_cheak)-i-1]:break
            else:
                result += 1
            for i in range(len(y_cheak)//2):
                if y_cheak[i] != y_cheak[len(x_cheak)-1-i]:break
            else:
                result += 1
    print('#{} {}'.format(num, result))
