import sys; sys.stdin = open('5189.txt', 'r')

def perm(k):
    global result
    if k == N:
        arr.append(0)
        check = 0
        for i in range(len(arr)-1):
            check += office[arr[i]][arr[i+1]]
        arr.pop()
        result = min(result, check)
    else:
        for i in range(k, N):
            if k == 0 and i != 0: continue
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

T= int(input())
for tc in range(1, T+1):
    result = 1000000
    N = int(input())
    office = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    perm(0)
    print('#{} {}'.format(tc, result))






