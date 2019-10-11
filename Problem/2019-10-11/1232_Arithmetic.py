import sys; sys.stdin = open('1232.txt', 'r')

def postorder(s):
    if s < 0: return
    for i in range(2**(s+1), 2**s-1, -1):
        if i > N: continue
        if node[i] == '-':
            x, y = int(arr2[i][2]), int(arr2[i][3])
            node[i] = node[x] - node[y]
        if node[i] == '+':
            x, y = int(arr2[i][2]), int(arr2[i][3])
            node[i] = node[x] + node[y]
        if node[i] == '*':
            x, y = int(arr2[i][2]), int(arr2[i][3])
            node[i] = node[x] * node[y]
        if node[i] == '/':
            x, y = int(arr2[i][2]), int(arr2[i][3])
            node[i] = node[x] / node[y]
    postorder(s-1)

for tc in range(1, 11):
    N = int(input())
    node = [0 for _ in range(N+1)]
    arr2 = [['0']] + [input().split() for _ in range(N)]
    for i in range(30):
        if N < 2**(i+1):
            level = i
            break
    for i in range(1, N+1):
        arr = arr2[i]
        idx = int(arr[0])
        if arr[1].isdecimal():
            node[idx] = int(arr[1])
        else:
            node[idx] = arr[1]
    postorder(level)
    print('#{} {}'.format(tc, int(node[1])))



