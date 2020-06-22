import sys; sys.stdin = open('1004.txt', 'r')

T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    N = int(input())
    for i in range(N):
        x, y, r = map(int, input().split())
        r **= 2
        length_1 = (x1 - x) ** 2 + (y1 - y) ** 2 < r
        length_2 = (x2 - x) ** 2 + (y2 - y) ** 2 < r
        if length_1 or length_2:
            if length_1 != length_2:
                res+=1
    print(res)
