import sys; sys.stdin = open('5207.txt', 'r')

def BinarySearch(lo, hi, search):
    global cnt, check
    mid = (lo + hi) // 2
    if [lo, hi, mid] == check:
        return
    check = [lo, hi, mid]
    print(search, A[mid])
    print(lo, hi, mid)
    print()
    if A[mid] == search:
        cnt += 1
        return

    # if mid == hi or lo == mid:
    #     return
    elif A[mid] > search:
        BinarySearch(lo, mid - 1, search)
    elif A[mid] < search:
        BinarySearch(mid + 1, hi, search)



T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    print(A)

    for i in B:
        check = []
        BinarySearch(0, N-1, i)

    print('#{} {}'.format(tc, cnt))

