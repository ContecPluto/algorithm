import sys; sys.stdin = open('1808.txt', 'r')

def check(k, CX, N):
    global flag
    if k == N:
        print('찾음')
        flag = 1
        return
    for i in arr:
        if i == CX[k]:
            chose.append(i)
            check(k + 1, CX, N)

def comb(div, num):
    global flag
    if flag == 1:
        return
    if div > int(X):
        return
    # print(div, num, num%div)
    # print(div)
    if div == num:
        flag = 1
        print('찾음')
        return

    if num%div >= 100:
        return
    if num%div == 0:
        CX = list(map(int, str(num//div)))
        check(0, CX, len(CX))
    for i in arr:
        comb((div*10) + i, num)
        div_num = div
        for j in range(1, 3):
            # div_num = (div_num * 10) + i
            # comb(div_num, num)
            # comb((div * 10) + i, num)
            comb(((div * 10) + i) ** j, num)
            comb(((div * 10) + i) * (div ** j), num)
            # comb(((div * 10) + i) ** (j - 1), num)
            # comb(((div*10) + i) * ((div*10) + i), num)
        # comb(((div*10) + i) * div, num)
        if i == 0 or i == 1: continue
        comb(div * i, num)


T = int(input())
for tc in range(T):
    print('tc:',tc+1)
    flag = 0
    arr = list(map(int, input().split()))
    X = input()
    first_check = list(map(int, X))
    length = len(first_check)
    chose = []
    arr = [i for i in range(len(arr)) if arr[i] == 1]
    check(0, first_check, length)
    print(arr, X)
    for i in arr:
        if i == 0: continue
        if flag == 1: continue
        comb(i, int(X))
    print()
