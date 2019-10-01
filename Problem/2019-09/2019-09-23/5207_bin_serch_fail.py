import sys; sys.stdin = open('5207.txt', 'r')

def BinarySearch(lo, hi, search):
    global cnt, check
    mid = (lo + hi) >> 1
    if lo > hi:
        return
    if A[mid] == search:
        cnt += 1
    elif A[mid] > search:
        if check:
            if check[-1] == 1:
                return
        check.append(1)
        BinarySearch(lo, mid - 1, search)
    elif A[mid] < search:
        if check:
            if check[-1] == 2:
                return
        check.append(2)
        BinarySearch(mid + 1, hi, search)
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        check = []
        BinarySearch(0, N - 1, i)
    print('#{} {}'.format(tc, cnt))

