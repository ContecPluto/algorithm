import sys; sys.stdin = open('1204.txt', 'r')

T = int(input())
for tc in range(1):
    num = input()
    arr = [0] * 101
    for i in list(map(int, input().split())):
        arr[i] += 1
    max_num = 0
    idx = 0
    for i in range(101):
        if arr[i] >= max_num:
            max_num = arr[i]
            idx = i
    print('#{} {}'.format(num, idx))