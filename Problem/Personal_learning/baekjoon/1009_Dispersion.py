# res_arr = [[] for _ in range(11)]
# for i in range(1, 11):
#     j = 1
#     while not (i ** j) % 10 in res_arr[i]:
#         res_arr[i].append((i ** j) % 10)
#         j += 1
#
#     if len(res_arr[i]) == 1:
#         for j in range(3):
#             res_arr[i].append(res_arr[i][0])
#     elif len(res_arr[i]) == 2:
#         res_arr[i].append(res_arr[i][0])
#         res_arr[i].append(res_arr[i][1])
# print(res_arr)

res_arr = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 4, 8, 6], [3, 9, 7, 1],
           [4, 6, 4, 6], [5, 5, 5, 5], [6, 6, 6, 6], [7, 9, 3, 1],
           [8, 4, 2, 6], [9, 1, 9, 1], [10, 10, 10, 10]]
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    a = a % 10
    if a:
        c = (b % 4) - 1
        print(res_arr[a][c])
    else:
        print(10)