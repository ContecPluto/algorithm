import sys; sys.stdin = open('4112.txt', 'r')

dx = [-1, -1, 0, 0, 1, 1]
dy = [0, -1, -1, 1, 0, 1]


i = 0
start = 1
arr = [[1]]
while start < 10000:
    i += 1
    for j in range(start+1, start + i):
        arr[i-1].append(j)
    start += i
    arr.append([start])
def move(s):
    x, y = s
    for i in range(6):
        tx = x + dx[i]
        ty = y + dy[i]
        # if tx < ty:continue
        if maping.get((tx,ty)) == None:
            maping[(tx,ty)] = 1
        else:
            pass
        # move((tx,ty))

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    for i in range(len(arr)):
        if N in arr[i]:
            minji = (i, arr[i].index(N))
            break
    for i in range(len(arr)):
        if M in arr[i]:
            piramid = (i, arr[i].index(M))
            break
    maping= {minji: 0}
    move(minji)
