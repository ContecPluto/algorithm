from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

N = int(input())
heap = []
result = ""

for i in range(N):
    x = int(input())
    if x:
        heappush(heap, [abs(x), x])
    else:
        if not heap:
            result += "0\n"
        else:
            result += f"{heappop(heap)[1]}\n"
        
print(result)