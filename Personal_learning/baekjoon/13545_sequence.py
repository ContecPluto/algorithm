N = int(input())
sequence = [0] + list(map(int, input().split()))
M = int(input())

for i in range(1, N+1):
    sequence[i] += sequence[i-1]

result = ""
for m in range(M):
    i, j = map(int, input().split())
    i -= 1
    val = j - i - abs(sequence[j] + sequence[i])
    result += f"{val}\n"
print(result, end="")
