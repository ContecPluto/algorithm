from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

N = int(input())
arr = []
result = ""
for i in range(N):
    x = int(input())
    if x:
        heappush(arr, -x)
    else:
        if arr:
            result += "{}\n".format(-heappop(arr))
        else:
            result += "0\n"
print(result, end="")
