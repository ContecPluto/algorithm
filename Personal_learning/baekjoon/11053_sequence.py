from sys import stdin

N = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j])
    else:
        dp[i] += 1
print(max(dp))
