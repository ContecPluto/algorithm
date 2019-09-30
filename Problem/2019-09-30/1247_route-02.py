import sys; sys.stdin = open('1247.txt', 'r')

def perm(k, distance):
    global result
    if distance + abs(arr[k][0] - arr[k-1][0]) + abs(arr[k][1] - arr[k-1][1]) >= result:
        return
    if k == N + 1:
        total = 0
        for n in range(k, len(arr)):
            total += abs(arr[k][0] - arr[k-1][0]) + abs(arr[k][1] - arr[k-1][1])
        result = min(result, distance + total)
        return

    for i in range(k, N + 1):
        arr[k], arr[i] = arr[i], arr[k]
        perm(k + 1, distance + abs(arr[k][0] - arr[k-1][0]) + abs(arr[k][1] - arr[k-1][1]))
        arr[k], arr[i] = arr[i], arr[k]



T = int(input())
for tc in range(1, T+1):
    result = 100000
    N = int(input())
    arr = list(map(int, input().split()))
    arr = [arr[i:i+2] for i in range(0, len(arr), 2)]
    arr[1], arr[-1] = arr[-1], arr[1]
    perm(1, 0)
    print('#{} {}'.format(tc, result))
