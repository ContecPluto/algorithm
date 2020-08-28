def solution(citations):
    citations.sort(reverse=True)
    citations = [0] + citations
    answer = max([min(citations[i], i) for i in range(1, len(citations))])
    return answer

solution([3, 0, 6, 1, 5, 2])