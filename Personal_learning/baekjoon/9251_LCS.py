s1 = ' ' + input()
s2 = ' ' + input()
dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[i][j])
