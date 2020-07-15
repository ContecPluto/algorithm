# N = int(input())
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ex_result = {}
# for i in range(N-1):
#     value = []
#     for j in arr:
#         if j%10 == 0:
#             value.append(j*10 + j % 10 + 1)
#         elif j%10 == 9:
#             value.append(j*10 + j % 10 - 1)
#         else:
#             value += [j*10 + j % 10 + 1, j*10 + j % 10 - 1]
#     arr = list(value)

#     result = dict()
#     for x in range(10):
#         result[x] = 0

#     cnt = 0
#     for y in arr:
#         result[int(str(y)[-1])] += 1

#     for key, value in result.items():
#         if key == 0:
#             if value == 0:
#                 cnt += 1
#             else:
#                 cnt += value * 1
#         elif key == 9:
#             cnt += value * 1
#         else:
#             cnt += value * 2
#     print(cnt)
# print(len(arr))

# 간단한 코딩으로 각각의 값이 얼마가 나오는지 확인하였다.
# 계단수는 각각 0, 9의 개수 * 1, 1 ~ 8의 개수 * 2의 형태로 늘어난다.
def DP(n):
    if result.get(n):
        return result[n]
    else:
        result[n] = [0] * 10
        arr = DP(n-1)
        for x in range(10):
            if x == 0:
                result[n][x + 1] = 1 * arr[x] 
            elif x == 9:
                result[n][x - 1] = 1 * arr[x]
            else:
                result[n][x + 1] = 1 * arr[x]
                result[n][x - 1] = 1 * arr[x]
        return result[n]


N = int(input())
result = {1: [0] * 10}
for i in range(1, 10):
    result[1][i] = 1
print(sum(DP(N))%1000000000)
