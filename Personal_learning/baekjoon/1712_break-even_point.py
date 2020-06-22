import sys; sys.stdin = open('1712.txt')    

A, B, C = map(int, input().split(' '))
if B < C:
    print(int(A/(C-B)) + 1)
else:
    print(-1)

