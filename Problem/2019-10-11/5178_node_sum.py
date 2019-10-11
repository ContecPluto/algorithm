import sys; sys.stdin = open('5178.txt', 'r')

def inorder(s):
    if s > N: return
    inorder(2 * s)
    inorder(2 * s + 1)
    num1, num2 =0, 0
    if 0 < s*2 <= N:
        num1 =  node[s*2]
        #왼쪽은 있고 오른쪽은 없는 경우를 대비 해서
        # N개의 노드를 가지고 있기 때문에 오른쪽이 없을 경우는 없다.
        if 0 < s*2+1 <= N:
            num2 = node[s*2+1]
        node[s] = num1 + num2

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    node = [0 for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        node[u] = v
    inorder(1)
    print('#{} {}'.format(tc, node[L]))
