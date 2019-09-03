import sys; sys.stdin = open('5097.txt', 'r')
from collections import deque
import queue


T = int(input())
for tc in range(1, T+1):
    N, M= list(map(int, input().split()))
    Q = deque(map(int, input().split()))

    for i in range(M):
        Q.append(Q.popleft())
    print('#{} {}'.format(tc, Q[0]))
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M= list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#
#     print('#{} {}'.format(tc, arr[M%N]))
#
