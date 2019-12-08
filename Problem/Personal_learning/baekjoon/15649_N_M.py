import sys; sys.stdin = open('15649.txt', 'r')

def comb(p):
    if p == M:
        print(*choose)
        return
    for i in range(1, N):
        if visit[i] == True: continue
        choose.append(i)
        visit[i] = True
        comb(p + 1)
        visit[i] = False
        choose.pop()

choose = []
N, M = map(int, input().split())
N += 1
visit = [False] * N
comb(0)
