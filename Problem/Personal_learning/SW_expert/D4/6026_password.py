import sys; sys.stdin = open('6026.txt', 'r')


def comb(b):
    global ans
    if b == N:
        if len(set(choose)) >= M:
            ans += 1
        return
    for i in range(M):
        choose.append(i)
        comb(b+1)
        choose.pop()


T = int(input())
for tc in range(3):
    M, N = map(int, input().split())
    ans = 0
    choose = []
    comb(0)
    print(ans)