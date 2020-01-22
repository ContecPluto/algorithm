import sys; sys.stdin = open('16637.txt', 'r')



def DFS(s, res):
    global result
    if min_val > res or max_val < res:
        return
    if s == N:
        result = max(res, result)
        return
    elif s == N - 2:
        num = int(arr[s+1])
        if arr[s] == '+':
            DFS(s+2, res + num)
        elif arr[s] == '-':
            DFS(s+2, res - num)
        else:
            DFS(s+2, res * num)
        return
    if arr[s] == '+':
        a = int(arr[s+1])
        b = arr[s + 2]
        c = int(arr[s+3])
        DFS(s + 2, res + a)
        if b == '*':
            DFS(s+4, res + (a * c))
        elif b == '+':
            DFS(s+4, res + (a+c))
        elif b == '-':
            DFS(s + 4, res + (a - c))
    elif arr[s] == '-':
        a = int(arr[s + 1])
        b = arr[s + 2]
        c = int(arr[s + 3])
        DFS(s + 2, res - a)
        if b == '*':
            DFS(s+4, res - (a * c))
        elif b == '+':
            DFS(s+4, res - (a+c))
        elif b == '-':
            DFS(s + 4, res - (a - c))
    elif arr[s] == '*':
        a = int(arr[s + 1])
        b = arr[s + 2]
        c = int(arr[s + 3])
        DFS(s + 2, res * a)
        if b == '*':
            DFS(s+4, res * (a * c))
        elif b == '+':
            DFS(s+4, res * (a+c))
        elif b == '-':
            DFS(s + 4, res * (a - c))

result = -0xfffffffff
min_val = (2 ** 31) * -1
max_val = 2 ** 31
N = int(input())
arr = list(input())
DFS(1, int(arr[0]))
print(result)
