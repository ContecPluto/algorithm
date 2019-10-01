import sys; sys.stdin = open('6485.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    count = [0] * 5001
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = [int(input()) for i in range(P)]

    for i, j in bus:
        for k in range(i, j + 1):
            count[k] += 1

    print('#{}'.format(tc), end=' ')
    for i in bus_stop:
        print(count[i], end=' ')
    print()

