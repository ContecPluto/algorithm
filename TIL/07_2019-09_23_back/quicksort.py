arr = [69, 10, 30, 2, 16, 8, 31, 22, 16, 57, 42, 32, 11, 54, 78, 97, 65, 46 ]
def quickSort(lo, hi):
    if lo >= hi: return
    i, j, pivot = lo, hi, arr[lo]
    while i  < j:
        while i <= hi and pivot >= arr[i]: i += 1
        while pivot < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    quickSort(lo, j - 1)
    quickSort(j + 1, hi)

def quickSort2(lo, hi):
    if lo> hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]

    quickSort2(lo, i - 1)
    quickSort2(i + 1, hi)

print(arr)
quickSort(0, len(arr)-1)
print(arr)

arr = [69, 10, 30, 2, 16, 8, 31, 22, 16, 57, 42, 32, 11, 54, 78, 97, 65, 46, 3, 533, 455, 432, 234, 654, 75, 464]
quickSort2(0, len(arr)-1)
print(arr)
