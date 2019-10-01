import sys; sys.stdin = open('1941.txt','r')

dx = [0,0,-1,1]
dy = [-1,1,0,0]

arr = [input() for _ in range(5)]

for i in range(5):
    for j in range(5):
        for x in range(j + 1, 6):

            # print(arr[i][j:x])

            li = len(arr[i][j:x])
            for y in range(0, li - 1):
                if y + 8 - x > 5: continue
                if j <= y <= y + 8 - x:
                    y_check = ''
                    for y2 in range(y, y + 8 - x):
                        y_check += arr[y2][i]
                print(arr[i][j+1:x])
                print('y는', y_check)

            # for y in range(0, 5)



