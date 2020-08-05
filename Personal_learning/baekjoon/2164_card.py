from collections import deque

N = int(input())
if N == 1:
    print(1)
else:
    arr  = deque(range(2, N+1, 2))
    if N % 2:
        arr.rotate(-1)

    while len(arr) != 1:
        arr.popleft()
        arr.rotate(-1)
    print(arr.pop())