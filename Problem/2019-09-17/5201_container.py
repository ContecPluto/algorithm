import sys; sys.stdin = open('5201.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    freight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    move = [False for _ in range(N)]
    result = 0

    for i in truck:
        for j in range(N):
            if i >= freight[j] and move[j] == False:
                move[j] = True
                result += freight[j]
                break
    print('#{} {}'.format(tc, result))
