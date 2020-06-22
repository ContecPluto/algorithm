import sys; sys.stdin = open('1941.txt','r')

dx = [0,0,-1,1]
dy = [-1,1,0,0]
downword = ''
arr = [input() for _ in range(5)]

for i in range(5):
    for j in range(5):
        for x in range(j + 1, 6):
            if len(arr[i][j:x]) < 3: continue
            n= 7 - len(arr[i][j:x])
            print('줄',arr[i][j:x], n, j ,x)
            for y in range(j, j+x):
                for z in range(0,5):
                    if z <= j < z+n: continue
                    for z2 in range(z, z + n):
                        if z2 == y: continue
                        print(y, z2)






            # for y in range(0, 5)



