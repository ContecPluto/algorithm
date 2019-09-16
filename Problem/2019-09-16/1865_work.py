import sys; sys.stdin = open('1865.txt', 'r')

def perm(k):
    global result
    if k == R:
        j = arr[0][choose[0]]/100
        for i in range(1, R):
            j *= arr[i][choose[i]]/100
        result = max(result, round(j*100, 7))
    else:
        for i in range(k, R):
            choose[i], choose[k] = choose[k], choose[i]
            perm(k + 1)
            choose[i], choose[k] = choose[k], choose[i]

T = int(input())
for tc in range(1):
    result = 0
    R = int(input())
    choose = list(range(R))
    arr = [list(map(int, input().split())) for _ in range(R)]
    perm(0)
    print(result)
