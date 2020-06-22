import sys; sys.stdin = open('3074.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = sorted([int(input()) for _ in range(N)])
    _arr = []
    chk = arr[0] * M
    for i in arr:
        for j in range(1, M+1):
            if i * j > chk:
                break
            _arr.append(i * j)
    _arr.sort()
    print('#{} {}'.format(tc, _arr[M-1]))