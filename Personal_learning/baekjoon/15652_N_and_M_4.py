def comb(s, p):
    if p == M:
        print(*choose)
        return
    for i in range(s, N):
        choose[p] = i
        comb(i, p + 1)


N, M = map(int, input().split(' '))
N += 1
choose = [0] * M
comb(1, 0)
