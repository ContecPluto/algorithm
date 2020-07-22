N, K = map(int, input().split(" "))
stuff = [[0,0]] + [list(map(int, input().split(" "))) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(1, N + 1):
    w, v = stuff[i]
    for j in range(K - w, -1, -1):
        dp[w + j] = max(dp[w + j], dp[j] + v)
print(dp[K])