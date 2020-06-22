import sys; sys.stdin = open('1206.txt', 'r')
for tc in range(1, 11):
    N, arr, answer = int(input()), tuple(map(int, input().split())), 0
    for i in range(2, N-2):
        check = sorted(arr[i-2:i+3])
        if arr[i] == check[4]:
            answer += arr[i] - check[3]
    print('#{} {}'.format(tc, answer))