# https://www.acmicpc.net/problem/2566

result = -1
position = [0, 0]

for i in range(9):
    arr = list(map(int, input().split()))

    for j in range(9):
        if result < arr[j]:
            result = arr[j]
            position = [i + 1, j + 1]

print(result)
print(*position)