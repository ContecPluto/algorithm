import sys; sys.stdin = open('2817.txt', 'r')
T = int(input())
for tc in range(1, T+ 1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cnt = 0
    for subset in range(1 << N):
        check = 0
        for j in range(N):
            if subset & (1 <<j):
                check += arr[j]
            # print()
        if check == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))