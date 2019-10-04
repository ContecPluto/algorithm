from datetime import timedelta
from time import time, strftime, localtime

def subset(k, N): #k는 찾을 숫자
    if not memo[k-1] and not memo[k]:
        subset(k - 1, N)
    if not memo[k]:
        for i in memo[k-1]:
            memo[k].append(i)
            check = i.copy()
            check.append(k)
            memo[k].append(check)
    else:
        return memo[k]
    if k == N:
        memo[k].sort()
        return memo[k]

# def subset2(k):
#     global memo
#     if not memo[k]:
#         for subset in range(1 << N):
#             A, B = [], []
#             for j in range(N):
#                 if subset & (1 << j):
#                     # print(arr[j], end=' ')
#                     A.append(arr[j])
#                 else:
#                     B.append(arr[j])
#             print(A,B)
#             memo[k].append([A, B])
#         return memo[k]
#     else:
#         return memo[k]





def log(s):
    global start
    start = time()
    print('시작 >>>> ', s)

def endlog():
    line = "=" * 40
    elapsed = time() - start
    print("실행 시간: ", elapsed)
    print('종료 >>>> ')
    print(line)
# log('memo')
memo = [[] for _ in range(100)]
# # memo[0], memo[1] = [[], [0], []], [[], [0], [0, 1], [1]]
# for i in range(1):
#     subset(9, 9)
# # print(memo[9])
# endlog()

# log('비트 메모')
arr = [0,1,2,3,4,5,6,7,8,9]
N = len(arr)
# for i in range(3):
#     subset2(N)
# print(memo[8])
#
for re in range(1):
    for subset in range(1 << N):
        print(subset, end = '>')
        for j in range(N):
            if subset & (1 <<j):
                # pass
                print(arr[j], end=' ')
            # print()
        print()
# print(subset)

endlog()