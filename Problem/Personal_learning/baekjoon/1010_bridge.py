import sys; sys.stdin = open('1010.txt', 'r')

facktoria = [1] * 31
for i in range(2, 31):
    facktoria[i] = facktoria[i-1] * i

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    res = facktoria[M] // (facktoria[M-N] * facktoria[N])
    print(res)

