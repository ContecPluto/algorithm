N = int(input())
sequence = list(map(int, input().split()))
dp = [[0, [sequence[_]]] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if sequence[i] > sequence[j] and dp[i][0] < dp[j][0]:
            dp[i] = [dp[j][0], dp[j][1] + [sequence[i]]]
    dp[i][0] += 1
    
result = max(dp)
print(result[0])
print(*result[1])