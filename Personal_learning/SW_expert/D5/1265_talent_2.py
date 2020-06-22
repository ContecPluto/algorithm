import sys; sys.stdin = open('1265.txt', 'r')






T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    val = N//P
    P2 = N - val * P
    result = val ** abs(P - P2) * (val + 1) ** P2
    print('#{} {}'.format(tc, result))

    # arr = [N//P for i in range(P)]
    # for i in range(1, N - sum(arr) + 1):
    #     arr[i] += 1
    # result = 1
    # for i in arr:
    #     result *= i
    # print('#{} {}'.format(tc, result))
