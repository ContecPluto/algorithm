import sys; sys.stdin=open('1486.txt','r')

def comb(s, answer):
    global result
    if answer >= B:
        if answer >= result:
            return
        else:
            result = answer
    for i in range(s, N):
        comb(i + 1, answer + arr[i])

T = int(input())
for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = 500000
    comb(0, 0)
    print('#{} {}'.format(tc, result-B))
