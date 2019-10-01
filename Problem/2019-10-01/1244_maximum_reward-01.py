import sys; sys.stdin = open('1244.txt','r')

def perm(s):
    global result, check
    # print(arr)
    if check[:s] > arr[:s]:
        return
    if s == N:
        if result < int(''.join(arr)):
            result = int(''.join(arr))
            check = arr[:]
        return
    if s >= len(arr)-1:
        if (N-s)%2 == 1:
            arr[-2], arr[-1] = arr[-1], arr[-2]
            perm(N)
            arr[-2], arr[-1] = arr[-1], arr[-2]
        else:
            perm(N)
        return

    if arr[s] == max(arr[s+1:]):
        s += 1
    for i in range(s, len(arr)):
        if arr[s] > arr[i]: continue
        arr[s], arr[i] = arr[i], arr[s]
        perm(s + 1)
        arr[s], arr[i] = arr[i], arr[s]




T = int(input())
for tc in range(1, T+1):
    index = 1
    arr, N = map(int, input().split())
    arr = list(str(arr))
    result = 0
    check = arr[:]
    perm(0)
    if result == 0:
        result = ''.join(arr)
    print('#{} {}'.format(tc, result))


