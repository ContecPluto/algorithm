dx = [-1, +1]

N = int(input())
arr = [0xfffffffff] * N
origin = set(range(N))
matrix = [[0] * N for _ in range(N)]
for x in range(N):
    matrix[x] = list(map(int, input().split(" ")))
    if x == 0: continue
    for i in range(3):
        num = 0xffffffffff
        for j in range(3):
            if i == j: continue
            num = min(num, matrix[x][i] + matrix[x-1][j])
        matrix[x][i] = num
print(min(matrix[-1]))
