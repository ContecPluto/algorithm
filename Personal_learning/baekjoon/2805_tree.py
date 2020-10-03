from sys import stdin
from collections import Counter
input = stdin.readline

N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

start = 1
end = max(trees.keys())

while start <= end:
    mid = (start+end) // 2
    cut = 0
    for tree, cnt in trees.items():
        if tree > mid:
            cut += (tree - mid) * cnt

    if M <= cut:
        start = mid + 1
    elif M > cut:
        end = mid - 1
    
print(end)