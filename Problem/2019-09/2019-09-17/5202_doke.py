import sys;sys.stdin = open('5202.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    doke = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda doke: doke[1])
    result = [doke[0]]

    for i in range(1, N):
        if result[-1][1] <= doke[i][0]:
            result.append(doke[i])
    print('#{} {}'.format(tc, len(result)))






