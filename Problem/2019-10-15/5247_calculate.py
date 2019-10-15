import sys; sys.stdin = open('5247.txt', 'r')
from collections import deque

def calculate(N, M, s):
    global ans
    Q = deque()
    Q.append(N)
    while Q:
        t = Q.popleft()
        if t > M + 10 or t < 0: continue
        if t == M:
            ans = chk.get(t)
            return
        for i in range(4):
            if i == 0:
                num = t * 2
            elif i == 1:
                num = t - 10
            elif i == 2:
                num = t - 1
            elif i == 3:
                num = t + 1
            if 0 < num < M + 500:
                if chk.get(t) + 1 < chk.get(num):
                    chk[num] = chk.get(t) + 1
                    Q.append(num)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = M//2
    chk = {}
    for i in range(M + 10000):
        chk[i] = 0xfffff
    chk[N] = 0
    calculate(N, M, 0)
    print('#{} {}'.format(tc, chk.get(M)))