import sys; sys.stdin = open('1002.txt', 'r')

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    r_sum = (r1 + r2) ** 2
    r_dif = (r1 - r2) ** 2
    if d:
        if r_sum == d or r_dif == d:
            print(1)
        elif r_sum > d and r_dif < r2:
            print(2)
        else:
            print(0)
    else:
        if r1 == r2:
            print(-1)
        else:
            print(0)
