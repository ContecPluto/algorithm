from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
sequence = [0] * N
sequence[0] = 1

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            sequence[i] = max(sequence[i], sequence[j])
    else:
        sequence[i] += 1
print(max(sequence))
