result = ""

T = int(input())
for tc in range(T):
    K = int(input()) + 1
    arr = [0] + list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]
    for i in range(1, K-1):
        dp[i][i+1] = arr[i] + arr[i+1]  

    for i in range(1, K):
        arr[i] += arr[i-1]

    for i in range(2, K-1):
        for j in range(1, K-i):
            ls = [dp[j][k] + dp[k+1][j+i] for k in range(j, j+i)]
            dp[j][i+j] = min(ls) + arr[j+i] - arr[j-1]
    result += "{}\n".format(dp[1][K-1])
print(result, end="")
