import sys; sys.stdin = open('15666.txt', 'r')

def comb(p, num, res):
    if p == M:
        print(*res)
        return
    for i in arr:
        if i < num: continue
        comb(p + 1, i, res+[i])


N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
comb(0, 0, [])

