N = 5
arr = [[1, 2, 3, 4, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9]]


for idx in range(2):    
    for x in range(N):
        print(arr[idx][x], end = ' ')
    
    for y in range(1, N-idx):
        print(arr[y][N-idx-1], end = ' ')

    for x in range(N-2, -1+idx, -1):
        print(arr[N-1-idx][x], end = ' ')

    for y in range(N-2, 0+idx, -1):            
        print(arr[y][idx], end=' ')



# for x in range(N):
#     print(arr[0][x], end =' ')

# for y in range(1, N):
#     print(arr[y][4], end = ' ')

# for x in range(N-2, -1, -1):
#     print(arr[4][x], end = ' ')

# for y in range(N-2, 0, -1):
#     print(arr[y][0], end = ' ')

# for x in range(N-1):
#     print(arr[1][x], end = ' ')

# for y in range(1, N-1):
#     print(arr[y][3], end = ' ')

# for x in range(N-2, 0, -1):
#     print(arr[3][x], end = ' ')

# for y in range(N-2,1,-1):    
#     print(arr[y][1], end = ' ')

# for x in range(N-3, N-2):
#     print(arr[2][x], end = ' ')







        



