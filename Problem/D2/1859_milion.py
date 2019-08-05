import sys
sys.stdin = open('1859.txt', 'r')
T = int(input())

 
for num in range(T):
    days = input()
    prices = list(map(int, input().split()))
    total = 0
    midle_price = 0
    max_price = 0
    count=0
    for i in range(len(prices)):
        if i == 0:
            max_price = max(prices[i::])

        if max_price == prices[i]:
            total += (max_price * count) - midle_price
            midle_price, count = 0, 0
            max_price = max(prices[i::])

        if prices[i] < max_price:
            # total += max_price - prices[i]
            midle_price += prices[i]
            count += 1



    print('#{} {}'.format(num+1, total))
        
            

