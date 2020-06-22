import sys; sys.stdin = open('6855.txt', 'r')

def comb(p, s):
    global answer
    if s == K:
        length = [0xffff] * N
        check = check_index - set(choose)
        for choice in choose:
            for index in check:
                if length[index] > abs(arr[choice] - arr[index]):
                    length[index] = abs(arr[choice] - arr[index])
        total = 0
        for idx in check:
            total += length[idx]
        answer = min(answer, total)

    for i in range(p, N):
        choose.append(i)
        comb(i + 1, s + 1)
        choose.pop()

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if N > K:
        answer = 0xffffff
        choose = []
        check_index = set([i for i in range(N)])
        comb(0, 0)
    else:
        answer = 0

    print('#{} {}'.format(tc, answer))