import sys; sys.stdin = open('2817.txt', 'r')
def comb(s, p, check):
    global cnt
    if check >= K:
        if check == K:
            cnt += 1
        return
    for i in range(s, N):
        comb(i + 1, p + 1, check + arr[i])

T = int(input())
for tc in range(1, T+ 1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cnt = 0
    comb(0, 0, 0)
    print('#{} {}'.format(tc, cnt))