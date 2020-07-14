import sys

N = int(sys.stdin.readline())
ex_line = list(map(int, sys.stdin.readline().split(" ")))

for i in range(1, N):
    arr = list(map(int, sys.stdin.readline().split(" ")))
    arr[0] += ex_line[0]
    arr[i] += ex_line[i-1]
    for j in range(1, i):
        arr[j] += max(ex_line[j], ex_line[j-1])
    ex_line = arr
arr = ex_line

print(max(arr))
