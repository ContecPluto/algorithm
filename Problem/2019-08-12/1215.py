import sys
sys.stdin = open('1215.txt','r')

for num in range(1, 11):
    # print('시작')
    N = int(input())
    arr = [input() for _ in range(8)]
    result = 0

    for idx in range(8):
        for s in range(8-N+1):
            e = s + N - 1
            for i in range(N//2):
                if arr[idx][s + i] != arr[idx][e - i]: break
            else:
                result += 1
            for i in range(N//2):
                if arr[s + i][idx] != arr[e - i][idx]: break
            else:
                result += 1

            # x_cheak, y_cheak = '', ''
            # for z in range(y, y+N):
            #     x_cheak += words[x][z]
            #     y_cheak += words[z][x]
            #     # print(x_cheak, y_cheak)

            # for i in range(len(x_cheak)//2):
            #     if x_cheak[i] != x_cheak[len(x_cheak)-i-1]:break
            # else:
            #     result += 1
            # for i in range(len(y_cheak)//2):
            #     if y_cheak[i] != y_cheak[len(x_cheak)-1-i]:break
            # else:
            #     result += 1
    print('#{} {}'.format(num, result))
