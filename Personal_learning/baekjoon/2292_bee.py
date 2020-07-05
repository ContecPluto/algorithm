# https://www.acmicpc.net/problem/2292

result = 1
N = int(input())

N -= 1
while N > 0:
    N -= 6 * result
    result += 1
print(result)