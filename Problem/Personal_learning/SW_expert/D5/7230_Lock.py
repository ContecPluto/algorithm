import sys; sys.stdin = open('7230.txt', 'r')

def perm(p):
    global ans, arr
    if p == N:
        if not int(''.join(arr))%K:
            ans += 1
        return
    for i in range(p, N):
        arr[i], arr[p] = arr[p], arr[i]
        perm(p+1)
        arr[i], arr[p] = arr[p], arr[i]

T = int(input())
for tc in range(1, T+1):
    ans = 0
    N = int(input())
    arr = list(input().split())
    K = int(input())
    perm(0)
    print('#{} {}'.format(tc, ans))