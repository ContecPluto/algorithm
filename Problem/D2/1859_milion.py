import sys
sys.stdin = open('1859.txt', 'r')
T = int(input())
 
for num in range(T):
    days = input()
    prices = list(map(int, input().split()))
    total = 0
    # max_price = max(prices)
    count = 0

    #while문 도중에 멈춤
    #     max_price = max(prices[count::])
    #     total -= sum(prices[count:prices.index(max_price)+1])
    #     total += max_price*len(prices[count:prices.index(max_price)+1])
    #     count = prices.index(max_price)+1

    max_price = prices.pop()

    for i in range(len(prices)):
        count = prices.pop()
        if max_price <= count:
            max_price = count 
        total += max_price - count
        




    print('#{} {}'.format(num+1, total))

