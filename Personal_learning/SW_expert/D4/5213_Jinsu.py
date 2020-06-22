import sys; sys.stdin = open('5213.txt', 'r')

max_num = (10 ** 6) + 1
arr = [0] * max_num
for j in range(1, max_num + 1, 2):
    for i in range(j, max_num, j):
        arr[i] += j
for i in range(1, max_num):
    arr[i] += arr[i-1]

T = int(input())
for tc in range(1, T+1):
    L, R = map(int, input().split())
    print('#{} {}'.format(tc, arr[R]-arr[L-1]))


