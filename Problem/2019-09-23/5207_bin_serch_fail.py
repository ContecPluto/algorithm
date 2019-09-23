import sys; sys.stdin = open('5207.txt', 'r')

def BinarySearch(lo, hi, search):
    global cnt, check
    mid = (lo + hi) // 2
    if lo > hi:
        return

    # print(mid, A[mid], search)
    if A[mid] == search:
        cnt += 1
        return
    elif A[mid] > search:
        check.append(2)
        BinarySearch(lo, mid - 1, search)
    elif A[mid] < search:
        check.append(1)
        BinarySearch(mid + 1, hi, search)

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        check = []
        BinarySearch(0, len(A)-1, i)
    print('#{} {}'.format(tc, cnt))

