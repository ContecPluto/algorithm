#셀렉션 정렬
arr = [64, 25, 10, 22, 11]
N = len(arr)
#[0, n-1] 최솟값의 위치를 찾는다


for i in range(N - 1):
    minIdx = i
    for j in range(i + 1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)
