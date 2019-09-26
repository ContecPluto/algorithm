import sys; sys.stdin = open('1799.txt', 'r')

def comb(k,s):
    if k == R:
        print(choose)
    else:
        for i in range(s, N):
            choose.append(arr[i])
            comb(k + 1, i)
            choose.pop()

arr = 'ABCDEFGHIJ'
N,R = len(arr), 4
choose = []
comb(0, 0)
