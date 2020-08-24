N = int(input())
dp = [[0] * N for _ in range(N)]
procession = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    x, y = procession[i]
    z = procession[i+1][1]
    dp[i][i+1] = x * y * z

arr = list(range(N))
for i in range(1, N):
    for j in range(N-i):
        dp[j][i+j] = 0xfffff
        for k in range(j, j+i):
            print(j, i+j, j, k)
            dp[j][i+j] = min(dp[j][i+j], (dp[j][k] + dp[k+1][i+j] + procession[j][0] * procession[i+j][0] * procession[i+j][1]))
print(dp[0][N-1])