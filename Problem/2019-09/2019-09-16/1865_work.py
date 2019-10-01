import sys; sys.stdin = open('1865.txt', 'r')

def perm(k, n, used, result):
    global total
    check = 1
    # max_check = [0, 0]
    #
    # if order:
    #     for x in range(0, len(order)):
    #         check *= arr[x][order[x]] / 100

    if k == R:
        total = max(total, result*100)
        # print(tc, total)
        # print(order)

    for i in range(n):
        if used & (1 << i): continue
        order.append(choose[i])
        j = check * arr[k][order[k]] / 100
        if j * 100 < result:
            order.pop()
            continue
        num = result*j
        perm(k + 1, n, used | (1 << i), num)
        order.pop()

T = int(input())
for tc in range(1, T+1):
    total = 1
    order = []
    R = int(input())
    choose = list(range(R))
    arr = [list(map(int, input().split())) for _ in range(R)]
    perm(0, len(choose), 0, 1)
    print('#{} {:.6f}'.format(tc, round(total, 6)))

