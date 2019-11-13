import sys; sys.stdin = open('4008.txt', 'r')
operator = ['+', '-', '*', '/']

def make(num, plus, dif, mul, div, ans):
    global max_val, min_val
    num += 1
    if plus != 0:
        make(num, plus-1, dif, mul, div, ans + arr[num])
    if dif != 0:
        make(num, plus, dif - 1, mul, div, ans - arr[num])
    if mul != 0:
        make(num, plus, dif, mul - 1, div, ans * arr[num])
    if div != 0 and arr[num] != 0:
        make(num, plus, dif, mul, div - 1, int(ans / arr[num]))
    if num == N:
        max_val = max(max_val, ans)
        min_val = min(min_val, ans)

T = int(input())
for tc in range(1, T+1):
    max_val, min_val = -100000000, 100000000
    N = int(input())
    plus, dif, mul, div = map(int, input().split())
    arr = list(map(int, input().split()))
    make(0, plus, dif, mul, div, arr[0])
    print('#{} {}'.format(tc, max_val - min_val))
