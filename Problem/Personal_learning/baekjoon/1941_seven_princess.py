import sys; sys.stdin = open('1941.txt','r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(s, k):
    global result, check
    if k == 7:
        print(check)
        if check.count('S') >= 4:
            result += 1
        return
    x,y = s
    visit[x][y] = True
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 5 and 0 <= ty < 5:
            if visit[tx][ty] == False:
                check.append(arr[tx][ty])
                DFS([tx, ty], k + 1)
                check.pop()


arr = [input() for _ in range(5)]
visit = [[False for _ in range(5)] for _ in range(5)]
result = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            check = ['S']

            DFS([i, j], 0)
print(result)

