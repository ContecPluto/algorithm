# 순열 생성
arr = 'ABCDE'
N = len(arr)
R = 3
choice = ['']*R

def backtrack(k, start):
    if k == R:
        print(choice)
    else:
        for i in range(start, N):
            choice[k] = arr[i]
            backtrack(k + 1, i + 1)
backtrack(0, 0)




# for i in range(N - 2):
#     for j in range(i + 1, N-1):
#         for k in range(j + 1, N ):
#             print(arr[i], arr[j], arr[k])

