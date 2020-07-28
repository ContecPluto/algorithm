from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

result = [False, False, True, True] + [False, True] * (max(numbers) // 2 + 1)
for number in range(3, int(max(numbers) ** 0.5) + 1, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
result = [i for i in numbers if result[i]]

print(len(result))