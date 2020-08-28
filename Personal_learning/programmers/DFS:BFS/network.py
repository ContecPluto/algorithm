from collections import deque

def solution(n, computers):
    answer = 1
    N = len(computers)
    G = [[] for _ in range(len(computers))]
    visit = [False] * N
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if computers[i][j]:
                G[i].append(j)
                
    Q = deque([0])
    while Q:
        while Q:
            s = Q.popleft()
            visit[s] = True
            for p in G[s]:
                if not visit[p]:
                    Q.append(p)
                    
        if sum(visit) != N:
            Q.append(visit.index(False))
            answer += 1
    return answer

# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])