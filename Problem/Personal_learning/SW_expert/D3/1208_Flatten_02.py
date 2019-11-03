import sys;sys.stdin = open('1208.txt', 'r')

for tc in range(1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    for i in range(N):
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()
    print('#{} {}'.format(tc, max(arr)-min(arr)))
