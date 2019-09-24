import sys; sys.stdin = open('5208.txt', 'r')

def busStop(charge, change):
    global min_change
    # print(charge, check)
    if charge >= N-1:
        min_change = min(min_change, change-1)
        print(check, change-1)
        return
    if min_change < change:
        return
    for i in range(charge+1, bus[charge]+charge+1):
        if i >= N: continue
        check.append(i)
        busStop(i, change+1)
        check.pop()

T = int(input())
for tc in range(1, T+1):
    min_change = 10000
    bus = list(map(int, input().split()))
    N = bus[0]
    check = [1]
    busStop(1, 0)
    print('#{} {}'.format(tc, min_change))

