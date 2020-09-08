N = int(input())
dp = [0xfffff] * (N+1)

square = [i * i for i in range(1, 317)]
for i in square:
    if i > N:
        break
    dp[i] = 1

for i in range(1, N+1):
    for j in square:
        if j > i:
            break
        dp[i] = min(dp[i], dp[i-j] + dp[j])
print(dp[N])

