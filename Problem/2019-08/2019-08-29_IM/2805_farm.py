import sys; sys.stdin = open('2805.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for i in range(N)]
    midle = N//2
    total = 0

    for x in range(N//2):
        total += sum(farm[x][midle-x:midle+x+1:])
        total += sum(farm[N-x-1][midle-x:midle+x+1])
    total += sum(farm[midle])

    print('#{} {}'.format(tc, total))

