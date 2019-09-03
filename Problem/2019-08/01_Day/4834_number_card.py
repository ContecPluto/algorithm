import sys
sys.stdin = open('4834.txt', 'r')
T = int(input())

for num in range(T):
    numbers = []
    card = int(input())
    N = int(input())
    my_max=0
    my_int=0


    for number in str(N):
        numbers.append(number)


    for i in numbers:
        if my_max < numbers.count(i):
            my_max = numbers.count(i)
            my_int = int(i)
            if my_max == numbers.count(i):
                if my_max > my_int:
                    my_max == my_int


    print('#{} {} {}'.format(num+1, my_int, my_max))


