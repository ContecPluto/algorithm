import sys
sys.stdin = open('1210.txt', 'r')

for num in range(10):
<<<<<<< HEAD
    n = input()
=======
    n = int(input())
>>>>>>> e10eac0fa983828e598fdad714cf16738df35a5e
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for x in range(100):
        if ladder[99][x] == 2:
            y = x
<<<<<<< HEAD
            break    
    x = 99
    # print(y)

    # y = ladder[99].index(2)
    
    while x != 0:
        # print(x,y)
        ladder[x][y] = 0
        for i in range(3):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= ty <= 99:
                if ladder[tx][ty] != 0:
                    # print(tx,ty)
                    # print('잡힘?')
                    x = tx
                    y = ty
                    break
        if x == 0:
            print('#{} {}'.format(n, y))
            break
    
=======
            break

    x = 99
    # # print(n, y)
    # while x != 0:
    #     # print(x,y)
    #     ladder[x][y] = 0
    #     for i in range(3):
    #         tx = x + dx[i]
    #         ty = y + dy[i]
    #         if 0 <= ty <= 99:
    #             if ladder[tx][ty] != 0:
    #                 # print(tx,ty)
    #                 # print('잡힘?')
    #                 x = tx
    #                 y = ty
    #                 break
    # print('#{} {}'.format(num+1, y))
    # dir = 0   #0:위, 1:왼쪽, 2:오른쪽
    # while x:
    #     if dir != 2 and y - 1 >= 0 and ladder[x][y-1]:   #왼쪽
    #         y, dir = y - 1, 1
    #     elif dir != 1 and y+1 < 100 and ladder[x][y+1]: #오른쪽
    #         y, dir = y + 1, 2
    #     else: #위
    #         x, dir = x - 1, 0

    # dir = 0   #0:위, 1:왼쪽, 2:오른쪽
    while x:
        if y - 1 >= 0 and ladder[x][y-1]:   #왼쪽
            while y - 1 >= 0 and ladder[x][y - 1]:
                y -= 1
            x -= 1
        elif y+1 < 100 and ladder[x][y+1]: #오른쪽
            while y + 1 < 100 and ladder[x][y + 1]:
                y += 1
            x -= 1
        else: #위
            x -= 1
    print(y)

    # def DFS(x, y):
    #     if x == 0: return y
    #     ladder[x][y] = 0
    #     if y-1 >= 0 and ladder[x][y - 1]:
    #         return DFS(x, y-1)
    #     elif y + 1 < 100 and ladder[x][y + 1]:
    #         return DFS(x, y + 1)
    #     else:
    #         return DFS(x - 1, y)
    # print(DFS(x, y))



>>>>>>> e10eac0fa983828e598fdad714cf16738df35a5e

