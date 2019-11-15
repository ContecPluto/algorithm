import sys; sys.stdin = open('2105.txt', 'r')
dx = [+1, 1, -1, -1]
dy = [-1, 1, 1, -1]
def DFS(s, direction):
    global answer, choose2
    tx, ty = s
    if direction == 3:
        if abs(tx - start[0]) != abs(ty - start[1]):
            return
    previos_choose2 = choose2[::]
    x = tx + dx[direction]
    y = ty + dy[direction]
    while 0 <= x < N and 0 <= y < N:
        if choose2[arr[x][y]] == 0:
            choose2[arr[x][y]] = 1
            if direction != 3:
                DFS([x, y], direction + 1)
        else:
            if [x, y] == start:
                answer = max(sum(choose2), answer)
            break
        x += dx[direction]
        y += dy[direction]
    choose2 = previos_choose2[::]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    choose2 = [0] * 101
    for high in range(N):
        for width in range(N):
            choose2[arr[high][width]] = 1
            start = [high, width]
            DFS(start, 0)
            choose2[arr[high][width]] = 0
    if answer == 0:
        answer = -1
    print('#{} {}'.format(tc, answer))