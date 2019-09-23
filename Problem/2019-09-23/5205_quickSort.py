import sys; sys.stdin = open('5205.txt', 'r')

def quickSort(lo, hi):
    if lo >= hi: return
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]: i += 1
        while pivot < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    quickSort(lo, j - 1)
    quickSort(j + 1, hi)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(0, N-1)
    print('#{} {}'.format(tc, arr[N//2]))