N = int(input())
dp = [0] * (N+3)
dp[1] = 1
dp[2] = 1
dp[3] = 2
for n in range(4, N+1):
    dp[n] = dp[n-1] + dp[n-2]
print(dp[N])