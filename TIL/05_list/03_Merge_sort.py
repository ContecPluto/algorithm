def merge_sort(m):
    if len(m) <= 1: #사이즈가 0이거나 1인경우, 바로 리턴
        return m


    #1. Divide
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    #리스트의 크기가 1이 될 떄까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0: #양쪽 리스트에원소가 남아있을 경우
        #두 서브 리스트에 첫 원소들을 비교하여 작은것부터 result에 추가합
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0 : #왼쪾 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

a = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(a))
