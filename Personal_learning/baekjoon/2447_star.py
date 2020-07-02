N = int(input())
star = [["*"] * N for _ in range(N)]
arr = [1]
while arr[-1] != N:
    arr.append(arr[-1] * 3)
arr.pop()

for k in arr:
    arr2 = []
    for i in range(k, N, k):
        if i//k%3 == 1:
            for x in range(i, i+k):
                arr2.append(x)
            
    for i in arr2:
        for j in arr2:
            star[i][j] = " "

for i in star:
    print("".join(i))