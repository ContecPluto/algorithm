# 풀이 1
# import sys

# N = int(input())
# matrix = [[0] * N for _ in range(N)]
# matrix[0] = list(map(int, sys.stdin.readline().split(" ")))
# for x in range(1, N):
#     matrix[x] = list(map(int, input().split(" ")))
#     if x == 0: continue
#     for i in range(3):
#         num = 0xffffffffff
#         for j in range(3):
#             if i == j: continue
#             num = min(num, matrix[x][i] + matrix[x-1][j])
#         matrix[x][i] = num
# print(min(matrix[-1]))


# 풀이 2 같은 방식(간단 코딩)
import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split(" ")))]
for x in range(1, N):
    matrix.append(list(map(int, sys.stdin.readline().split(" "))))
    matrix[x][0] += min(matrix[x-1][1], matrix[x-1][2])
    matrix[x][1] += min(matrix[x-1][0], matrix[x-1][2])
    matrix[x][2] += min(matrix[x-1][0], matrix[x-1][1])
print(min(matrix[-1]))