import sys;sys.stdin = open('15650.txt', 'r')

def comb(s, p):
    if p == M:
        print(*choose)
        return
    for i in range(s, N):
        choose.append(i)
        comb(i + 1, p + 1)
        choose.pop()

choose = []
N, M = map(int, input().split())
N += 1
comb(1, 0)
