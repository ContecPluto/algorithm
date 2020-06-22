dx = [0, 0, -1, +1]
dy = [1, -1, 0, 0]

def DFS(s, v, per):
    global check
    x, y = v
    if s == N:
        return
    for i in range(4):
        if robot[i] == 0: continue
        tx = x + dx[i]
        ty = y + dy[i]
        if visit[tx][ty] == False:
            visit[tx][ty] = True
            DFS(s+1, [tx, ty], per*robot[i])
            visit[tx][ty] = False
        else:
            check += per*robot[i]


import sys; sys.stdin=open('1405.txt','r')
robot = list(map(int, input().split()))
N = robot.pop(0)
for i in range(4):
    robot[i] /= 100
check = 0
visit = [[False for _ in range(28)] for _ in range(28)]
visit[0][0] = True
DFS(0, [0, 0], 1)
print('{:.10f}'.format(1-check))