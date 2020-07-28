from math import sqrt

N, M = map(int, input().split())
result = [False, False, True, True] + [False, True] * (M // 2 + 1)
for number in range(3, int(M ** 0.5) + 1, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
result = [i for i in range(N, M+1) if result[i]]
print(*result, sep="\n")
