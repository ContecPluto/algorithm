import sys; sys.stdin = open('5204.txt', 'r')

def mergeSort(lo, hi): #매개변수 --> 문제의 크기
    # print(lo, hi)
    global cnt
    if lo == hi: return
    #분할
    mid = (lo + hi - 1) >> 1
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)
    i, j, k= lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    if arr[mid] > arr[hi]:
        cnt += 1
    # print(tmp)
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr =list(map(int, input().split()))
    tmp = [0] * N
    mergeSort(0, N-1)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))
