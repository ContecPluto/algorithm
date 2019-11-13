import sys;sys.stdin = open('2117.txt','r')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            visit = [[False] * N for _ in range(N)]
            # k = 1
            arr = {(i, j)}
            home = 0
            if array[i][j] == 1:
                home += 1
                if home * M >= 2:
                    answer = max(answer, home)

            for k in range(2, N+2):
                arr2 = list(arr)
                arr = set()
                for x, y in arr2:
                    if visit[x][y] == True: continue
                    visit[x][y] = True
                    for z in range(4):
                        tx, ty = x+dx[z], y+dy[z]
                        if 0 <= tx < N and 0 <= ty < N:
                            if visit[tx][ty] == True: continue
                            arr.add((tx, ty))
                for x, y in arr:
                    if array[x][y] == 1:
                        home += 1
                if home*M >= k * k + (k-1)*(k-1):
                    answer = max(answer, home)
    print('#{} {}'.format(tc, answer))












