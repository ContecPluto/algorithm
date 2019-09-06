import sys; sys.stdin = open('1961.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    print('#{} '.format(tc))
    for i in range(N):
        x = N - i - 1
        result1, result2, result3 = '', '', ''
        for j in range(N-1, -1, -1):
            y = N-j-1
            result1 += arr[j][i]
            result2 += arr[x][j]
            result3 += arr[y][x]
        print(result1, result2, result3)

