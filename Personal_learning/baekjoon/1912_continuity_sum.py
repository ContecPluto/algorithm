N = int(input())
arr = list(map(int, input().split(" ")))
dp = [arr[0]] + [-1001] * (N - 1)
for i in range(1, N):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
print(max(dp))