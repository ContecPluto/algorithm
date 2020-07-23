N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
result = 0
# arr = []
# for i in range(N):
#     num = int(input())
#     if num > K:
#         for j in range(i+1, N):
#             input()
#         break
#     else:
#         arr.append(num)

for i in range(len(arr)-1, -1, -1):
    result += K//arr[i]
    K %= arr[i]
print(result)