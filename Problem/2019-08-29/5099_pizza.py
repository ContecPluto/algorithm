import sys; sys.stdin = open('5099.txt','r')
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    Ci = deque(map(int, input().split()))
    for i in range(len(Ci)):
        Ci[i] = [Ci[i], i]
    Q = deque()

    # print(Ci)
    for i in range(N):
        check = Ci.popleft()
        Q.appendleft(check)
    # print(Q)

    # print()

    while len(Q) != 1:
        check = Q.pop()
        check[0] = check[0]//2
        if check[0] == 0:
            if Ci:
                Q.appendleft(Ci.popleft())
        else:
            Q.appendleft(check)


        # print(Q)
    print('#{} {}'.format(tc, Q[0][1]+1))

