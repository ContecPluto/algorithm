import sys;sys.stdin = open('3752.txt','r')

# def comb(k, s, result):
#     if result in answer[k].keys():
#         return
#     else:
#         answer[k][result] = choose
#     for i in range(s, N):
#         comb(k+1, i+1, result + arr[i])


# cnt = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = {0}
    for i in arr:
        temp = list(answer)
        for j in range(len(temp)):
            answer.add(temp[j]+i)
    print('#{} {}'.format(tc, len(answer)))

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     my_list = list(map(int, input().split()))
#     my_len = len(my_list)
#     my_sum = sum(my_list)
#     dp = [1] + [0] * my_sum
#     temp = [0]
#     count = 1
#
#     for i in my_list:
#         print(i)
#         for j in range(len(temp)):
#             print(temp)
#
#             # print(i + temp[j])
#             if dp[i + temp[j]] == 0:
#                 dp[i + temp[j]] = 1
#                 # print(i+temp[j])
#                 temp.append(i + temp[j])
#                 count += 1
