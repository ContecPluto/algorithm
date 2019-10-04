from time import time, strftime, localtime
from datetime import timedelta

#재귀적 순열
arr = [0, 1,2,3, 4]
N = len(arr)
# for i in range(N):
#     arr[0], arr[i] = arr[i], arr[0]
#     for k in range(1, N):
#         arr[1], arr[k] = arr[k], arr[1]
#         for j in range(2, N):
#             arr[2], arr[j] = arr[j], arr[2]
#             print(arr)
#             arr[2], arr[j] = arr[j], arr[2]
#         arr[1], arr[k] = arr[k], arr[1]
#     arr[0], arr[i] = arr[i], arr[0]

# def log(s):
#     global start
#     start = time()
#     print('시작 >>>> ', s)
#
# def endlog():
#     line = "=" * 40
#     elapsed = time() - start
#     print("실행 시간: ", elapsed)
#     print('종료 >>>> ')
#     print(line)
#
# log('일반순열')
# def perm(k):
#     global cnt
#     if k==N:
#         cnt += 1
#         print(arr, end=' ')
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k + 1)
#             arr[k], arr[i] = arr[i], arr[k]
# cnt = 0
# perm(0)
# print()
# print(cnt)
# endlog()

# def nCr(n, r):
#     if n == r or r == 0:
#         return 1
#     return nCr(n-1, r-1) + nCr(n-1, r)
#
# print(nCr(5,3))
# print(nCr(10,4))
#
arr = 'ABCDEFGHIJ'
N,R = len(arr), 4
choose = []
# def comb(k,s):
#     if k == 7:
#         print(choose)
#     else:
#         for i in range(s, N):
#             choose.append(arr[i])
#             comb(k + 1, i)
#             choose.pop()
# comb(0, 0)

#메모이제이션 연습
def perm(z, n):
    global result, memo
    if not memo[n-1] and not memo[n]:
        perm(z-1, n-1)

    if not memo[n] and memo[n-1]:
        i = n - 1
        for j in range(len(memo[i])):
            for k in range(len(memo[i][j]) + 1):
                check = memo[i][j].copy()
                check.insert(k, i)
                # print(check)
                memo[i + 1].append(check)
                # if i == 10:
                #     print(i+1)
                #     print(memo[i+1])

    if z == n:
        result = memo[z]
        return result

# log('memo')
memo = [[] for _ in range(100)]
# memo[1] = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
memo[3] = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
# memo[2] = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]


perm(9, 9)
print(len(result))

# endlog()

