import sys; sys.stdin = open('4301.txt', 'r')

dx = [-2, 0, 2, 0]
dy = [0, -2, 0, 2]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    seed = []
    for i in range(M):
        for j in range(N)∑
            for k in range(4):
                tx = i + dx[k]
                ty = j + dy[k]
                if 0 <= tx < M and 0 <= ty < N:
                    if arr[tx][ty] != 0:
                        break
            else:
                arr[i][j] = 1
    total = 0
    for i in arr:
        total += sum(i)
    print('#{} {}'.format(tc, total))