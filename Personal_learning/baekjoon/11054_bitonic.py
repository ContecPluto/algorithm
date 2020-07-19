N = int(input())
sequence = list(map(int, input().split(" ")))
if N > 2:
    dp = [[0] * N for _ in range(2)]
    dp[0][0], dp[1][0] = 1, 1

    for k in range(2):
        for i in range(1, N):
            for j in range(i):
                if sequence[i] > sequence[j]:
                    dp[k][i] = max(dp[k][i], dp[k][j])
            dp[k][i] += 1
        sequence.reverse()
    result = 0

    dp[1].reverse()
    for i in range(N):
        result = max(result, dp[0][i] + dp[1][i])
    print(result - 1)
else:
    print(len(set(sequence)))