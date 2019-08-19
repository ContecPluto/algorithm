data = 'ABC'
n = len(data)

for i in range(n):
    for j in range(i, n):
        if i == j: continue
        for k in range(j, n):
            if i == j or j == k: continue
            print(data[i], data[j], data[k])