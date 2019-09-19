dx = [0, 0, -1, +1]
dy = [1, -1, 0, 0]

def DFS(s, v, per, visit):
    global check
    x, y = v
    if s == robot[0]:
        return
    for i in range(4):

        if robot[i+1] == 0: continue
        tx = x + dx[i]
        ty = y + dy[i]

        if [tx, ty] not in visit:
            visit.append([tx, ty])
            DFS(s+1,[tx, ty], per*robot[i+1]/100, visit)
            visit.pop()
        else:
            check += per*robot[i+1]/100

import sys; sys.stdin=open('1405.txt','r')
robot = list(map(int, input().split()))
check = 0
DFS(0, [0, 0], 1, [[0,0]])
# print(check)
print('{:.10f}'.format(1-check))