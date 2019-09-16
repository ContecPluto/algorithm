#재귀적 순열
arr = [1,2,3,4]
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


