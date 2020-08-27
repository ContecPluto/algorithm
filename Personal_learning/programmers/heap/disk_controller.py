from heapq import heappop, heapify

def solution(jobs):
    answer = 0
    end_point = 0
    jobs.sort()
    N = len(jobs)
    for i in range(N):
        arr = [[end_point + jobs[i][1], i, jobs[i][0]] for i in range(len(jobs)) if jobs[i][0] <= end_point]
        if not arr:
            arr = [[jobs[i][1] + jobs[i][0], i, jobs[i][0]] for i in range(len(jobs)) if jobs[0][0] == jobs[i][0]]
        heapify(arr)
        job = heappop(arr)
        jobs = [jobs[i] for i in range(len(jobs)) if i != job[1]]
        end_point = job[0]
        answer += job[0] - job[2]
    return answer//N

print(solution([[0,1],[1,2],[500,6],[500, 1]]))
# print(solution([[0, 3], [1, 9], [2, 6]]))