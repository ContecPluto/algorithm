import sys; sys.stdin = open('5204.txt', 'r')


def merge_sort(m):
    global cnt
    if len(m) <= 1: #사이즈가 0이거나 1인경우, 바로 리턴
        return m
    #1. Divide
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    #리스트의 크기가 1이 될 떄까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


def merge(left, right):
    result = []
    left.reverse()
    right.reverse()
    while len(left) > 0 and len(right) > 0: #양쪽 리스트에원소가 남아있을 경우
        #두 서브 리스트에 첫 원소들을 비교하여 작은것부터 result에 추가합
        if left[-1] <= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    if len(left) > 0 : #왼쪾 리스트에 원소가 남아있는 경우
        left.reverse()
        result.extend(left)
    if len(right) > 0:
        right.reverse()
        result.extend(right)
    return result


T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    print('#{} {} {}'.format(tc, merge_sort(list(map(int, input().split())))[N//2], cnt))
