import sys
sys.stdin = open('4835.txt', 'r')
T = int(input())

for num in range(T):
    N = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    my_sum = 0
    result = 0
    for i in range(0, len(arr)-N[1]+1):
        for j in range(i, i+ N[1]):
            result += arr[j]
            if i == 0:
                my_dif = result
        # print(result)
        if my_sum < result:
            my_sum = result
        elif my_dif > result:
            my_dif = result
        result = 0

    print('#{} {}'.format(num+1, my_sum-my_dif))



