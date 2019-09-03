import sys; sys.stdin = open('1220.txt','r')

for tc in range(1, 11):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    check = [[] for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if magnetic[y][x]:
                check[x].append(magnetic[y][x])

    for x in range(len(check)):
        for y in range(len(check[x])-1):
            if check[x][y] == 1 and check[x][y+1] == 2:
                count += 1
    print('#{} {}'.format(tc, count))




