D = ((-1, -1), (-1, 0))

def solution(triangle):
    answer = triangle[0][0]
    N = len(triangle)
    for x in range(1, N):
        M = len(triangle[x-1])
        for y in range(len(triangle[x])):
            num = 0
            for dx, dy in D:
                tx = x + dx
                ty = y + dy
                if 0 <= tx < N and 0 <= ty < M:
                    num = max(num, triangle[tx][ty])
            triangle[x][y] += num
    answer = max(triangle[-1])
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])