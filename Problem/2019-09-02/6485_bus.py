import sys; sys.stdin = open('6485.txt', 'r')

for tc in range(1, int(input()) + 1):
    count = [0] * 5001
    for i, j in [list(map(int, input().split())) for _ in range(int(input()))]:
        for k in range(i, j + 1):
            count[k] += 1

    print('#{}'.format(tc), end=' ')
    for i in [int(input()) for i in range(int(input()))]:
        print(count[i], end=' ')
    print()


