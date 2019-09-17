#재귀적 순열
arr = [0, 1,2]
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

def perm(k):
    if k==N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]
perm(0)

def nCr(n, r):
    if n == r or r == 0:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(5,3))
print(nCr(10,4))

arr = 'ABCDE'
N,R = len(arr), 3
choose = []

def comb(k,s):
    if k == R:
        print(choose)
    else:
        for i in range(s, N):
            choose.append(arr[i])
            comb(k + 1, i + 1)
            choose.pop()
comb(0, 0)

#메모이제이션 연습
# def perm(z, n):
#     global result, memo
#     if not memo[n-1] and not memo[n]:
#         perm(z-1, n-1)
#
#     if not memo[n] and memo[n-1]:
#         i = n - 1
#         for j in range(len(memo[i])):
#             for k in range(len(memo[i][j]) + 1):
#                 check = memo[i][j].copy()
#                 check.insert(k, i)
#                 # print(check)
#                 memo[i + 1].append(check)
#                 if i == 10:
#                     print(i+1)
#                     print(memo[i+1])
#
#     if z == n:
#         result = memo[z]
#         return result


