import sys; sys.stdin = open('2005.txt','r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result0 = [1]

    print('#{}'.format(tc))
    print(1)
    for i in range(1, N):
        result1 = []

        for j in range(i+1):
            if j == 0: result1.append(1); continue
            elif j == i: result1.append(1); continue
            result1.append(result0[j] + result0[j-1])
        print(' '.join(map(str, result1)))
        result0 = result1






