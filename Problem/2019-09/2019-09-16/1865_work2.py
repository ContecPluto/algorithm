import sys; sys.stdin = open('1865.txt', 'r')
import time

st = time.time()

def perm(k, n, used, result):
    global total
    if k == R:
        total = max(total, result*100)

    for i in range(n):
        if used & (1 << i) or result * arr[k][i] < total: continue
        # j = result * arr[k][choose[i]] / 100
        # if result * arr[k][i] < total:
        #     continue
        # print(total, j*100)
        perm(k + 1, n, used | (1 << i), result * arr[k][i]/100)

T = int(input())
for tc in range(1, T+1):
    total = 1
    R = int(input())
    arr = [list(map(int, input().split())) for _ in range(R)]
    perm(0, R, 0, 1)
    print('#{} {:.6f}'.format(tc, round(total, 6)))

print(time.time() - st)