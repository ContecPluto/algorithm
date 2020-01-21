import sys; sys.stdin = open('4530.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    arr2 = [0, 0]


    for num in range(2):
        change_num = 0
        if arr[num][0] == '-':
            idx = len(arr[num]) - 2
            start = 1
            for i in range(start, len(arr[num])):
                val = int(arr[num][i])
                val = val - 1 if val > 4 else val
                change_num -= val * (9 ** idx)
                idx -= 1
        else:
            idx = len(arr[num]) - 1
            start = 0
            for i in range(start, len(arr[num])):
                val = int(arr[num][i])
                val = val - 1 if val > 4 else val
                change_num += val * (9 ** idx)
                idx -= 1
        arr2[num] = change_num
    result = arr2[1] - arr2[0]
    if arr2[0] * arr2[1] < 0:
        result -= 1
    print('#{} {}'.format(tc, result))

