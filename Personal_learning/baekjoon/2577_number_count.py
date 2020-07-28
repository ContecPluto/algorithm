A = int(input())
B = int(input())
C = int(input())
arr = [0] * 10
for i in str(A * B * C):
    arr[int(i)] += 1
print(*arr, sep="\n")