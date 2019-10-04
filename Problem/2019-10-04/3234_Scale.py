import sys; sys.stdin = open('3234.txt', 'r')
from datetime import timedelta
from time import time, strftime, localtime
def log(s):
    global start
    start = time()
    print('시작 >>>> ', s)
def endlog():
    line = "=" * 40
    elapsed = time() - start
    print("실행 시간: ", elapsed)
    print('종료 >>>> ')
    print(line)


def perm(k):
    global cnt
    if k == N:
        

        # back=[0 for _ in range(N)]
        # # print('##############################################################')
        # for subset in subsets:
        #     A, B =0, 0
        #     if back == subset[:len(back)]: continue
        #     for index in range(N):
        #         if subset[index]:
        #             A += arr[index]
        #         else:
        #             B += arr[index]
        #         if A < B:
        #             break
        #     else:
        #         cnt += 1
        return
    for j in range(k, N):
        arr[j], arr[k] = arr[k], arr[j]
        perm(k+1)
        arr[j], arr[k] = arr[k], arr[j]

f_memo = [-1] * 100
f_memo[0], f_memo[1], f_memo[2] = 1, 1, 2
T = int(input())
for tc in range(1):
    chc = []

    log('시작')
    N = int(input())
    arr = list(map(int, input().split()))
    subsets = []
    cnt = 0
    for sub in range(1 << N):
        A = [0 for _ in range(N)]
        if sub & (1 << 0) == 0: continue
        a, b = 0, 0
        for i in range(N):
            if sub & (1 << i):
                A[i] += 1
                a += arr[i]
            else:
                b += arr[i]
        subsets.append(A)



    perm(0)
    print('#{} {}'.format(tc, cnt))
    endlog()
