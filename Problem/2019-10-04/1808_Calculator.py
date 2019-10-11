import sys; sys.stdin = open('1808.txt', 'r')

def check(k):
    global flag, cnt
    if k == N2:
        cnt[int(''.join(chose))] = N2
        flag = 1
        return
    for i in arr:
        if i == int(number[k]):
            chose.append(str(i))
            check(k + 1)

def calculator(s):
    global cnt
    answer = list(arr)
    print(arr)
    if s == len(arr): return
    for j in range(len(answer)):
        if answer[j] == 0: continue
        for i in range(j, len(answer)):
            num1, num2 = answer[j], answer[i]
            n = len(str(num2))
            num = num1 * (10 ** n) + num2
            if 0 < num <= N:
                arr.add(num)
                cnt[num] = cnt.get(num2) + cnt.get(num1)
            num = num1 * num2
            if 0 < num <= N:
                arr.add(num)
                cnt[num] = cnt.get(num2) + cnt.get(num1) + 1
            # print(arr)
            if num1 * 10 + num2 == int(number) or num1 * num2 == int(number):
                # print('야이야이야')
                return
    calculator(s+1)

T = int(input())
for tc in range(1, 30):
    chose = []
    arr = list(map(int, input().split()))
    arr = set([i for i in range(len(arr)) if arr[i] != 0 ])
    number = input()
    N = int(number)
    N2 = len(number)
    cnt = {}
    for i in arr:
        cnt[i] = 1
    # print(N, arr)
    print(tc, N)
    flag = 0
    # check(0)
    # if flag == 0:
    #     calculator(0)
    # # print(tc, arr)
    # # print(cnt)
    # if cnt.get(N) == None:
    #     print(tc, -1)
    # else:
    #     print(tc, cnt.get(N)+1)




