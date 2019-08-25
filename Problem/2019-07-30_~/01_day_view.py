import sys
sys.stdin = open('input.txt', 'r')

for num in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    # for i in range(2, len(arr)-2):
    #     for j in range(arr[i], 0, -1):
    #         for k in range(-2, 2, 1):
    #             if k == 0 : continue
    #             elif j <= arr[i+k]:
    #                 break
    #         else:
    #             count += 1


    for i in range(2, len(arr)-2):
        for j in range(arr[i], 0, -1):
            if j > arr[i-2] and j > arr[i-1] and j > arr[i+1] and j > arr[i+2]:
                count += 1

    # result = 0
    # for i in range(2,len(arr)-2 ):
    #     MAX = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
    #     if MAX < arr[i]:
    #         result += arr[i] - MAX


    print('#', num+1, ' ',  count, sep='')
    # print('#{} {}'.format(num+1, result))
