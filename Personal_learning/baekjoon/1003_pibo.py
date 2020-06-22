import sys; sys.stdin = open('1003.txt', 'r')

pibo = [[0, 0]] * 41
pibo[0] = [1, 0]
pibo[1] = [0, 1]

for i in range(2, 41):
    x, y = pibo[i-1], pibo[i-2]
    pibo[i] = [x[0] + y[0], x[1]+y[1]]

T = int(input())
for tc in range(T):
    n = int(input())
    print(*pibo[n])