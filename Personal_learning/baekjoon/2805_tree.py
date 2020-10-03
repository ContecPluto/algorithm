N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid

    if M <= cnt:
        start = mid + 1
    elif M > cnt:
        end = mid - 1
        
print(end)