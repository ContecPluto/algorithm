from sys import stdin
input = stdin.readline

T = int(input())
result = ""
for tc in range(T):
    k = int(input())
    n = int(input())
    arr = [list(range(n + 1))] + [[0] * (n+1) for _ in range(k)]
    for i in range(1, k + 1):
        arr[i][1] = arr[i-1][1]
        for j in range(2, n + 1):
            arr[i][j] = arr[i][j-1] + arr[i-1][j] 
    result += str(arr[k][n]) + "\n"
print(result, end="")