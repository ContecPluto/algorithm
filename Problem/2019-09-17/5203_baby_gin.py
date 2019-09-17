import sys; sys.stdin = open('5203.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    count = [[0 for _ in range(10)] for __ in range(2)]
    result = 0

    for i in range(12):
        if i % 2:
            count[1][card[i]] += 1
            if count[1][card[i]] >= 3:
                result = 2
                break
            for j in range(8):
                run1 = 1
                k = j + 0
                if count[1][j]:
                    while k < 9:
                        k += 1
                        if count[1][k] == 0:
                            break
                        elif count[1][k] > 0:
                            run1 += 1
                if run1 >= 3:
                    result = 2
                    break
            if run1 >= 3:
                break
        else:
            count[0][card[i]] += 1
            if count[0][card[i]] >= 3:
                result = 1
                break
            for j in range(8):
                run1 = 1
                k = j + 0
                if count[0][j]:
                    while k < 9:
                        k += 1
                        # print(k)
                        if count[0][k] == 0:
                            break
                        elif count[0][k] > 0:
                            run1 += 1
                if run1 >= 3:
                    result = 1
                    break
            if run1 >= 3:
                break
    print('#{} {}'.format(tc, result))





