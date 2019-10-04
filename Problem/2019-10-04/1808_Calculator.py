import sys; sys.stdin = open('1808.txt', 'r')

def comb(k, num):
    global flag
    if k == len(num):
        print(choose)
        flag = 1
        return
    for i in arr:
        if int(num[k]) == i:
            choose.append(i)
            comb(k + 1, X)
            choose.pop()

def comb2(k, num, div):
    global flag
    if num == 0:
        flag = 1
        return
    if flag == 1:
        return
    comb(0, str(num))
    for i in arr:
        comb2(k, int(num)//div, (div*10) + i)
        comb2(k, int(num)//div, (div*i))

T = int(input())
for tc in range(T):
    flag = 0
    arr = list(map(int, input().split()))
    X = input()
    arr = [i for i in range(len(arr)) if arr[i] == 1]
    choose = []
    num = int(X)
    comb(0, X)
    if flag == 0:
        for div in arr:
            if div == 0: continue
            comb2(0, X, div)


