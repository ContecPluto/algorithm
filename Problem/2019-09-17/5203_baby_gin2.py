import sys; sys.stdin = open('5203.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    count = [[0 for _ in range(10)] for __ in range(2)]
    result = 0

    for i in range(12):
        x = i % 2
        count[x][card[i]] += 1
        if count[x][card[i]] >= 3:
            result = x+1
            break
        for j in range(5):
            run1 = 1
            if count[x][j]:
                for k in range(j+1, j+4):
                    if count[x][k] == 0:
                        break
                    elif count[x][k] > 0:
                        run1 += 1
            if run1 >= 3:
                result = x + 1
                break
        if run1 >= 3:
            break
    print('#{} {}'.format(tc, result))




