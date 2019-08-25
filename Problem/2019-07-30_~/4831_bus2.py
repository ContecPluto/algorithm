

N, M = map(int, input().split())
arr =list(map(int, input().split()))

Sum = 0
for i in range(M):
    Sum += arr[i]

Min = Max = Sum

for i in range(N - M + 1):
    Sum += (arr[i+M]) - arr[i])
    Min = min(Min, Sum)
    Max = max(Max, Sum)

print('#{} {}',(test_case, Max - Min))