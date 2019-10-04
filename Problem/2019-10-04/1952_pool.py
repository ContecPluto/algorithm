import sys;sys.stdin = open('1952.txt', 'r')

def swim(k, money):
    global result
    if money >= result:
        return
    if k > N:
        result = money
        return
    if arr[k] == 0:
        swim(k+1, money)
        return
    swim(k + 1, money + (arr[k] * price[0])) #하루
    swim(k + 1, money + price[1]) #한 달
    swim(k + 3, money + price[2]) #세 달


T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    N = len(arr) - 1
    result = price[3]
    swim(0, 0)
    print('#{} {}'.format(tc, result))
