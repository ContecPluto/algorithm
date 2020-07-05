# https://www.acmicpc.net/problem/2292

result = 1
N = int(input())
start = 1
# N = 1
plus = 6
while N >= 0:
    print(N, result)
    result += 1
    plus += 6 * result
    N = N - 6 * result
print(result)