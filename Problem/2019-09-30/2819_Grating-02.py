import sys; sys.stdin = open('2819.txt', 'r')

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def DFS(x, y, k, result):
    if k == 0:
        answer.add(result)
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 4 and 0 <= ty < 4:
            DFS(tx, ty, k - 1, result + arr[tx][ty])

T = int(input())
for tc in range(1, T+1):
    arr = [tuple(input().split()) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, 6, arr[i][j])
    print('#{} {}'.format(tc, len(answer)))
