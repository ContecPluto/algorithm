def tournament(lo, hi):
    if lo == hi:
        return lo

    mid = int((lo + hi)/2)

    l = tournament(lo, mid)
    r = tournament(mid + 1, hi)

    if student[l] == 1:
        if student[r] == 1 or student[r] == 3:
            return l
        else:
            return r
    if student[l] == 2:
        if student[r] == 2 or student[r] == 1:
            return l
        else:
            return r
    if student[l] == 3:
        if student[r] == 3 or student[r] == 2:
            return l
        else:
            return r


import sys; sys.stdin = open('4880.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    student = list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(0, len(student) - 1) + 1))
