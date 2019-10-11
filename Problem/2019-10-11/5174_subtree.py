import sys; sys.stdin = open('5174.txt', 'r')

def preorder(s):
    global result
    if s == 0: return
    result += 1
    preorder(child[s][0])
    preorder(child[s][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # N는 루트, E는 간선수
    arr = list(map(int, input().split()))
    result = 0
    child = [[0, 0] for _ in range(E + 2)]
    for i in range(0, len(arr), 2):
        u, v = arr[i], arr[i+1]
        if child[u][0] == 0:
            child[u][0] = v
        else:
            child[u][1] = v
    preorder(N)
    print('#{} {}'.format(tc, result))

