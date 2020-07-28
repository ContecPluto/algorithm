from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

result = [False, False, True, True] + [False, True] * (M // 2)
for number in range(3, int(M ** 0.5) + 1, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
result = [i for i in range(N, M+1) if result[i]]

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)