words = input()
find = input()
arr = []
idx = 0
cnt = 0
n = len(find) - 1
pi = [0] * len(find) 
for i in range(2, len(find)):
    a, b = "", ""
    cnt = 0
    for j in range(i//2 + 1):
        if j == i - j: continue
        a += find[j]
        b = find[i-j] + b

    suffix = []
    prefix = []
    for x in range(len(a)):
        suffix.append(a[x])
        prefix.append(b[x])
        for y in range(x+1 , len(a)):
            suffix.append(suffix[-1] + a[y])
            prefix.append(prefix[-1] + b[y])

    for x in suffix:
        for y in prefix:
            if x == y:
                cnt = max(len(x), cnt)
    pi[i] = cnt
        
while idx + len(find) <= len(words):
    for i in range(len(find)):
        if words[i+idx] != find[i]:
            idx = idx - pi[i] + i + 1
            break 
    else:
        arr.append(idx+1)
        idx = idx - pi[i] + i
    print(idx, i, pi[i])
print(words[11])
print(len(arr))
print(*arr, sep=' ')

