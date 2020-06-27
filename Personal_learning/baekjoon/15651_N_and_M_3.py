def comb(p):
    if p == M:
        print(*choose)
        return
    for i in range(1, N):
        choose[p] = i
        comb(p + 1)


N, M = map(int, input().split(' '))
N += 1
choose = [0] * M
comb(0)
