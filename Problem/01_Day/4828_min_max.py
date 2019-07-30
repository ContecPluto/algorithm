import sys
sys.stdin = open('4828.txt', 'r')
T = int(input())
for num in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    my_max, my_min = arr[0], arr[0]

    for i in range(1, len(arr)):
        if arr[i] > my_max:
            my_max = arr[i]
        if arr[i] < my_min:
            my_min = arr[i]
    print('#{} {}'.format(num+1, my_max-my_min))
