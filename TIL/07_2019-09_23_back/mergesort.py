arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
def mergeSort(lo, hi): #매개변수 --> 문제의 크기
    print(lo, hi)
    if lo == hi: return
    #분할
    mid = (lo + hi) >> 1
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

    # print(tmp)
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]



mergeSort(0, len(arr) - 1)
print(arr)