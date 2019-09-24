import sys;sys.stdin=open('5209.txt','r')

def perm(k, answer):
    global result
    if answer > result:
        return
    if k == N-1:
        # print(arr, answer + make[k][arr[k]])
        result = min(result, answer + make[k][arr[k]] )
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, answer + make[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    make = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    result = 0
    for i in make:
        result += max(i)
    perm(0, 0)
    print('#{} {}'.format(tc, result))