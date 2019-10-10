import sys; sys.stdin = open('tree_input.txt', 'r')

def preorder(s):
    if s <= 0: return
    print(s, end=' ')
    preorder(child[s][0])
    preorder(child[s][1])

def inorder(s):
    if s <= 0: return
    inorder(child[s][0])
    print(s, end=' ')
    inorder(child[s][1])

def postorder(s):
    if s <= 0: return
    inorder(child[s][0])
    inorder(child[s][1])
    print(s, end=' ')

N = int(input())
arr = list(map(int, input().split()))
arr = [arr[i:i+2] for i in range(0, len(arr), 2)]
print(arr)
child = [[0, 0] for i in range(N+2)]
for i in range(N):
    u, v = arr[i]
    if child[u][0] == 0:
        child[u][0] = v
    else:
        child[u][1] = v
print('preorder :',end= ' ')
preorder(1)
print()
print('inorder :', end=' ')
inorder(1)
print()
print('postorder :', end=' ')
postorder(1)
