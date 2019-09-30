import sys; sys.stdin = open('1247.txt', 'r')

def perm(k, distance):
    global result
    if distance >= result:
        return
    if k == N + 1:
        total = 0
        for n in range(k, len(arr)):
            x = abs(route[arr[n]][0] - route[arr[n-1]][0])
            y = abs(route[arr[n]][1] - route[arr[n-1]][1])
            total += x + y
        result = min(result, distance + total)
        return

    for i in range(k, N + 1):
        arr[k], arr[i] = arr[i], arr[k]
        perm(k + 1, distance + abs(route[arr[k]][0] - route[arr[k-1]][0]) + abs(route[arr[k]][1] - route[arr[k-1]][1]))
        arr[k], arr[i] = arr[i], arr[k]



T = int(input())
for tc in range(1, T+1):
    result = 100000
    N = int(input())
    route = list(map(int, input().split()))
    arr = list(range(2, len(route)//2))
    route = [route[i:i+2] for i in range(0, len(route), 2)]
    arr = [0] + arr + [1]
    perm(1, 0)

    print('#{} {}'.format(tc, result))
    # print(route)
