from sys import stdin

N = int(stdin.readline())
wine = [0] + [int(stdin.readline()) for _ in range(N)]
if N > 1:
    matrix = [[0, 0] for _ in range(N + 1)] 
    result = wine[1] + wine[2]
    matrix[1][0], matrix[1][1], matrix[2][0], matrix[2][1] = wine[1], wine[1], wine[2], wine[1] + wine[2]
    for n in range(3, N+1):
        matrix[n][0] = max(matrix[n-2][0], matrix[n-2][1], matrix[n-3][0], matrix[n-3][1]) + wine[n]
        matrix[n][1] = matrix[n-1][0] + wine[n]
        result = max(result, matrix[n][0], matrix[n][1])
    print(result)
else:
    print(wine[1])