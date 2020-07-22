N, K = map(int, input().split(" "))
stuff = [[0,0]] + [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N)]
ran = set()
# if stuff[0][0] < K:
#     dp[stuff[0][0]] = stuff[0][1]
#     ran.add(stuff[0][0])
for i in range(1, N + 1):
    print(stuff[i][0])
    for j in range(1, stuff[i][0] + 1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuff[i][0]+stuff[i][1]])
    print(dp)
print(max(dp))