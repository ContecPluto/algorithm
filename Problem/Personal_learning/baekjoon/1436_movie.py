import sys; sys.stdin = open('1436.txt')

N = int(input()) - 1
res = 666
count = 1

while N:
    res += 1
    if '666' in str(res):
        N -= 1
print(res)