# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    # scoville.sort()
    heapify(scoville)

    while len(scoville) != 1:
        if scoville[0] >= K:
            return answer
        mix_food = heappop(scoville) + (heappop(scoville) * 2)
        heappush(scoville, mix_food)
        answer += 1

    if scoville[0] >= K:
        return answer
    return -1


print(solution([1], 7))