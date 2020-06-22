import sys; sys.stdin = open('2231.txt')

def part(s, val, n, x):
    global result
    if result: return
    if s == N:
        if val == target:
            result = x
        return
    for j in range(9, -1, -1):
        y = j * (10 ** n)
        part(s+1, val + y + j, n-1, x + y)

num = input()
target = int(num)
N = len(num)
result = 0
end = 9 if int(num[0]) == 9 else int(num[0]) + 1
for i in range(int(num[0])-1, end):
    part(1, i*10**(N-1) + i, N-2, i*10**(N-1))
    if result:
        break
print(result)