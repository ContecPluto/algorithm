import sys; sys.stdin = open('15486.txt', 'r')
input = sys.stdin.readlines

N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
for i in range(N-1, -1, -1):
    if consulting[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + 1], dp[consulting[i][0] + i] + consulting[i][1])
print(dp[0])