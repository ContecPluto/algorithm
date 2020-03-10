import sys; sys.stdin = open('13545.txt', 'r')

N = int(input())
arr = tuple(map(int, input().split(' ')))
M = int(input())
sum_arr = [0] * N

for i in range(N):
    if arr[i] == 0:
        sum_arr[0] = arr[i]
    else:
        sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(M):
    result = 0
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    value = sum_arr[y]
    if value:
        for j in range(x, y):
            if value == sum_arr[j]:
                result = y - j
            elif sum_arr[j] == 0:
                result = j + 1
    else:
        result = y + 1
    print(result)
