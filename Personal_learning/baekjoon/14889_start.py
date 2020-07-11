def comb(s, p):
    global result
    if result == 0:
        return
    if p == end:
        start = set(arr)
        link = set(origin) - start
        sum_start = 0
        sum_link = 0
        for x in start:
            for y in start:
                sum_start += S[x][y]

        for x in link:
            for y in link:
                sum_link += S[x][y]
        result = min(result, abs(sum_start - sum_link))
        return
    for i in range(s, N):
        arr.append(i)
        comb(i + 1, p + 1)
        arr.pop()


N = int(input())
end = N//2
origin = range(N)
S = [list(map(int, input().split(" "))) for _ in range(N)]
sum_S = [[0] * N for _ in range(N)]
arr = []
result = 0xfffffffff
comb(0, 0)
print(result)