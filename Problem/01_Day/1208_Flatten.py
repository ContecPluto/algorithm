import sys
sys.stdin = open('1208.txt', 'r')


for num in range(10):
    N = int(input())
    arr = list(map(int, input().split()))


    # index 사용
    # for i in range(N):
    #     arr[arr.index(max(arr))] -= 1
    #     arr[arr.index(min(arr))] += 1

    # for i in range(N):
    #     for j in range(len(arr)):
    #         if arr[j] == max(arr):
    #             arr[j] -= 1
    #             break
    #     for j in range(len(arr)):
    #         if arr[j] == min(arr):
    #             arr[j] += 1
    #             break

    for i in range(N):
        max_index = arr[0]
        min_index = arr[0]
        for j in range(len(arr)):
            if arr[j] > max_index:
                max_index = arr[j]
            if arr[j] < min_index:
                min_index = arr[j]
        arr[arr.index(max_index)] -= 1
        arr[arr.index(min_index)] += 1

    max_index = arr[0]
    min_index = arr[0]
    for j in range(len(arr)):
        if arr[j] > max_index:
            max_index = arr[j]
        if arr[j] < min_index:
            min_index = arr[j]
        
    print('#{} {}'.format(num+1, max_index-min_index))
