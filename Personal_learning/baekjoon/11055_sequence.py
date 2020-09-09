N = int(input()) + 1
sequence = [0] + list(map(int, input().split()))
dp = [0] * N
for i in range(1, N):
    value =  [dp[j] for j in range(0, i) if sequence[i] > sequence[j]]
    dp[i] = sequence[i] + max(value)
print(max(dp))


# N = int(input())
# sequence = list(map(int, input().split()))
# dp = [0] * 1001
# for i in sequence:
#     value =  dp[:i]
#     dp[i] = i + max(value)
# print(max(dp))