import sys; sys.stdin = open('14501.txt', 'r')

def back(i, start, k):
    global check, result
    k += 1
    if start <= N and start:
        # print(check[1:],start)
        total = 0
        if check[1] == 0:
            total += consulting[check[1]][1]
            # print(0,end=' ')
        for j in range(len(check[1:])):
            if check[j]:
                total += consulting[check[j]][1]
                # print(consulting[check[j]][1], end=' ')
        result = max(result, total)

    for i in range(start, N):
        if k == 1:
            check = [0 for _ in range(N+5)]
            check[k] = i
            # print(check,i)
            back(i, i + consulting[i][0], k)
        else:
            if i + consulting[i][0] <= N:
                # print(k, i)
                check[k] = i
                back(i, i + consulting[i][0], k)
            check[k+1] = 0
            # print(check[1:])
    k -= 1

    # print(check[1:])


N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
result = 0
check = [0 for _ in range(N+5)]
back(0, 0, 0)
print(result)
# print(4 + consulting[4][0])