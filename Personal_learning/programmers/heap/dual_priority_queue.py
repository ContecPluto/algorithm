from heapq import heappush, heappop, heapify, _heapify_max

def solution(operations):
    answer = []
    for operation in operations:
        command, num = operation.split(" ")
        if command == "I":
            heappush(answer, int(num))
        else:
            if answer:
                if num == "1":
                    _heapify_max(answer)
                else:
                    heapify(answer)
                heappop(answer)
                
    if not answer:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))