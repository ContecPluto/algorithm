from collections import deque
D = ((1, 0), (0, 1))

def solution(m, n, puddles):
    answer = 0
    max_value = 0xfffffff
    roadmap = {}
    for x, y in puddles:
        roadmap[y-1, x-1] = -1
    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        d, x, y = Q.popleft()
        d += 1
        if d > max_value:
            break

        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < n and 0 <= ty < m:
                if roadmap.get((tx, ty)) == -1: continue
                Q.append((d, tx, ty))
                if [tx, ty] == [n-1, m-1]:
                    if d == max_value:
                        answer += 1
                    elif d < max_value:
                        max_value = d
                        answer = 1
    return answer%1000000007



print(solution(4, 3, [[2, 2]]))