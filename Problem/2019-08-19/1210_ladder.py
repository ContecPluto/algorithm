import sys
sys.stdin = open('1210.txt', 'r')

for num in range(10):
    n = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for x in range(100):
        if ladder[99][x] == 2:
            y = x
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
    

