data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
count = [0]*7
for i in range(0, len(data)):
    for j in range(i):
        if data[i] >= data[j]:
            count[i] += 1
print(count)
