import sys; sys.stdin = open('1231.txt', 'r')

def inorder(s):
    if s == 0: return
    inorder(child[s][0])
    print(node[s], end='')
    inorder(child[s][1])

for tc in range(1, 11):
    N = int(input())
    child = [[0, 0] for _ in range(N + 1)]
    node = ' '
    for i in range(1, N+1):
        arr = input().split()
        node += arr[1]
        for idx, j in enumerate(range(2, len(arr))):
            child[i][idx] = int(arr[j])

    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()
