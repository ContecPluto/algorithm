from heapq import heappush, heappop

Q = []
result = ""

N = int(input())
for i in range(N):
    x = int(input())
    if x:
        heappush(Q, x)
    else:
        if not Q:
            heappush(Q, 0)
        result += f"{heappop(Q)}\n"
print(result)