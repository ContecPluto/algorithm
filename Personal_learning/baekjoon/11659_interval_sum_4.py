# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
result = []

# 각 구간 까지의 합을 미리 계산한다
for idx in range(1, n + 1):
    num_list[idx] += num_list[idx-1]

for _ in range(m):
    # i 시작점, j 종료지점
    i, j = map(int, input().split())

    # 종료지점 까지의 합에서 시작지점의 합을 빼서 계산한다.
    result.append(num_list[j] - num_list[i-1])

print(*result, sep="\n")