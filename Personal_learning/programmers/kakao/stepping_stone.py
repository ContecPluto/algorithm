def solution(stones, k):
    start = 0
    end = max(stones) + 1
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        triger = True
        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt == k:
                    triger = False
                    answer = mid
                    break
            else:
                cnt = 0

        if triger:
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
