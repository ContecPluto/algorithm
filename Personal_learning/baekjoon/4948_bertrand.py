from sys import stdin
input = stdin.readline

answer = ""
value = 123456 * 2
result = [False, False, True, True] + [False, True] * (value // 2)
dp = [0] * 246916
for number in range(3, int(value**0.5) + 1, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])

for num in range(1, len(result)):
    if result[num]:
        dp[num] = dp[num-1] + 1
    else:
        dp[num] = dp[num-1]

while True:
    N = int(input())
    if N:
        answer += str(dp[2*N] - dp[N]) + "\n"
    else:
        break
print(answer, end="")