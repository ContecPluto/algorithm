#이진 검색

arr = []
key = 123

# 후에 재귀로 다시볼것
def binarySearch(arr, key):
    # lo, hi = 0, len(arr) -1
    if lo>hi : return False
    while lo <= hi:
        mid = (lo + hi) >> 1
        if arr[mid] == key:
            return True
        if arr[mid] > key:
            return binarySearch(arr, lo, mid - 1, key)
        else:
            return binarySearch(arr, mid+1, hi, key)
    return -1