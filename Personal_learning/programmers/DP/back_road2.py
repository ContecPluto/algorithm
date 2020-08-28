D = ((-1, 0), (0, -1))

def solution(m, n, puddles):
    answer = 0
    m += 1
    n += 1
    roadmap = [[0]*m for _ in range(n)]
    roadmap[0][1] = 1
    for x, y in puddles:
        roadmap[y][x] = -1

    for x in range(1, n):
        for y in range(1, m):
            if roadmap[x][y] == -1: continue
            for dx, dy in D:
                tx = x + dx
                ty = y + dy
                if 0 <= tx < n and 0 <= ty < m:
                    if roadmap[tx][ty] == -1: continue
                    roadmap[x][y] += roadmap[tx][ty]
            print(roadmap)
    return roadmap[n-1][m-1]%1000000007

solution(4, 3, [[2, 2]])