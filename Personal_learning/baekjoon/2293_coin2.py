N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = [i for i in arr if i <= K]
result = 0

dp = [0 for i in range(K+1)]
dp[0] = 1
for i in arr:
    for j in range(i, K+1):
        dp[j] += dp[j-i]
print(dp[K])