import sys; sys.stdin = open('2819.txt', 'r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(s, k, result):
    if k == 7:
        answer[result] = 0
        return
    x, y = s
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 4 and 0 <= ty < 4:
            DFS([tx, ty], k + 1, result + arr[tx][ty])

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    answer = {}
    for i in range(4):
        for j in range(4):
            DFS([i, j], 0, '')
    print('#{} {}'.format(tc, len(answer)))
