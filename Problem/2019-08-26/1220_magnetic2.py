import sys; sys.stdin = open('1220.txt','r')

for tc in range(1, 11):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for x in range(N):
        check = 0
        for y in range(N):
            if magnetic[y][x]:
                if magnetic[y][x] == 1:
                    check = 1
                elif magnetic[y][x] == 2:
                    if check == 1:
                        count += 1
                    check = 2


    print('#{} {}'.format(tc, count))




