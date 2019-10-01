import sys; sys.stdin = open('6190.txt', 'r')

# def backtrack(k, start):
#     global result
#     if k == R:
#         multiply = choice[0] * choice[1]
#         check_multiply = str(multiply)
#         if len(check_multiply) > 1:
#             for k in range(len(check_multiply)-1):
#                 if check_multiply[k] > check_multiply[k+1]:
#                     break
#             else:
#                 result = max(result, multiply)
#     else:
#         for i in range(start, N):
#             choice[k] = arr[i]
#             backtrack(k + 1, i + 1)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
    # result = -1
    # R = 2
    # choice = [''] * R
    # backtrack(0, 0)
    #
    #
    # print('#{} {}'.format(tc, result))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = -1
    for i in range(N-1):
        for j in range(i+1, N):
            s = arr[i] * arr[j]
            t = s
            while t!= 0:
                a = t % 10  #1의 자리수
                t = t // 10 #1의 자리수를 제외한 나머지 수
                b = t % 10
                if b > a:
                    break
            if t == 0:
                if max_num <s: #최대값
                     max_num = s
    print(max_num)



