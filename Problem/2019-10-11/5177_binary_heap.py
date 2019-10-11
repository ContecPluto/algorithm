import sys;sys.stdin = open('5177.txt', 'r')

def inorder(s):
    if s == 0: return
    if 0 < s//2 < n:
        if heap[s//2] > heap[s]:
            heap[s//2], heap[s] = heap[s], heap[s//2]
    inorder(s//2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    result, n = 0, 0
    heap = [0]
    for i in num:
        n += 1
        heap.append(i)
        inorder(n)
    N = N//2
    while N != 0:
        result += heap[N]
        N //= 2
    print('#{} {}'.format(tc, result))
