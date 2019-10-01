import sys; sys.stdin = open('1244.txt','r')

def perm(s):
    global result, check
    if check[0] > arr[0]:
        return
    if s == N:
        if result < int(''.join(arr)):
            result = int(''.join(arr))
            check = arr[:]
        return

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[i]: continue
            arr[i], arr[j] = arr[j], arr[i]
            perm(s + 1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T+1):
    arr, N = input().split()
    arr, N = list(str(arr)), int(N)
    result = 0
    check = arr[:]
    perm(0)
    if result == 0:
        result = ''.join(arr)
    print('#{} {}'.format(tc, result))


