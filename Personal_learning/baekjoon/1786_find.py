words = input().rstrip()
find = input().rstrip()
idx = 0
n, m = len(find), len(words)
pi = [0] * len(find) 
arr = []

j=0
for i in range(1, n):
    while(j > 0 and find[i] != find[j]):
        j = pi[j - 1]
    if(find[i] == find[j]):
        j+=1
        pi[i] = j

cnt = 0
while idx + n <= m:
    if cnt < n and words[idx+cnt] == find[cnt]: 
        cnt += 1
        if cnt == n: 
            arr.append(idx + 1) 
    else: 
        if cnt == 0: 
            idx+=1 
        else: 
            idx += cnt-pi[cnt-1] 
            cnt = pi[cnt-1]
        
print(len(arr))
print(*arr, sep=' ')
