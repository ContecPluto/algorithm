import sys; sys.stdin = open('5176.txt', 'r')

def inorder(s):
    global idx
    if s < N:
        inorder(s*2)
        arr[s] = idx
        idx+=1
        inorder(s*2 + 1)
T = int(input())
for tc in range(1, T+1):
    idx = 1
    N = int(input()) + 1
    arr = [0 for _ in range(N)]
    inorder(1)
    N = (N-1)//2
    print('#{} {} {}'.format(tc, arr[1], arr[N]))