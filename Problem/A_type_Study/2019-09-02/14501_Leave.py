import sys; sys.stdin = open('14501.txt', 'r')

def back(i, start, k):
    global check, result
    k += 1
    if start <= N and start:
        total = 0
        if check[1] == 0:
            total += consulting[check[1]][1]
        for j in range(len(check[1:])):
            if check[j]:
                total += consulting[check[j]][1]
        result = max(result, total)

    for i in range(start, N):
        if k == 1:
            check = [0 for _ in range(N+5)]
            check[k] = i
            back(i, i + consulting[i][0], k)
        else:
            if i + consulting[i][0] <= N:
                check[k] = i
                back(i, i + consulting[i][0], k)
                check[k+1] = 0
    k -= 1



N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
result = 0
check = [0 for _ in range(N)]
back(0, 0, 0)
print(result)

