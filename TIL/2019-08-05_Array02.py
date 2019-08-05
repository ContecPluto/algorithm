N=5                   #N*N 배열
dx = [-1,+1,0,0]        #상하좌우
dy = [0,0,-1,+1]

arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]
total= 0


for x in range(N): #모든 행
    for y in range(N): #모든 열
        for i in range(4):            
            # [x][y]
            # 4방향의 인접위치좌표를 생성
            tx, ty = x + dx[i], y+dy[i]
            #경계 체크
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            total += abs(arr[tx][ty] - arr[x][y])
            # val = arr[x][y] - arr[tx][ty]
            # sum += (-val if val < 0 else val)
        # total -= 2*arr[x][y]
            
        print(total)
        print('------')



