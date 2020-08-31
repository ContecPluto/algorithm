from sys import stdin
input = stdin.readline
T = int(input())
result = ""

dp = [0] * (12)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for n in range(4, 12):  
    for i in range(n-3, n):
        dp[n] += dp[i]

for tc in range(T):
    N = int(input())
    result += f"{dp[N]}\n"
print(result, end="")