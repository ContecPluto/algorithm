import sys;sys.stdin = open('4366.txt', 'r')

T= int(input())
dx = {0:[1, 2], 1:[0, 2], 2 : [0, 1]}

for tc in range(1, T+1):
    origin_2 = list(map(int, input()))
    origin_3 = list(map(int, input()))
    x, y = len(origin_2), len(origin_3)

    for i in range(y):
        num3 = origin_3.copy()
        for j in range(x):
            num2 = origin_2.copy()
            if num2[j] == 1:
                num2[j] = 0
            else:
                num2[j] = 1
            for k in range(2):
                num3[i] = dx.get(origin_3[i])[k]
                check2 = 0
                check3 = 0
                for sum2 in range(x-1, -1, -1):
                    check2 += num2[x-sum2-1]*(2**sum2)
                for sum3 in range(y-1, -1, -1):
                    check3 += num3[y-1-sum3]*(3**sum3)
                if check2 == check3:
                    print('#{} {}'.format(tc, check2))
                    break
            if check2 == check3:
                break
        if check2 == check3:
            break
