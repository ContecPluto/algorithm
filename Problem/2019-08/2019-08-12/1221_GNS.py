import sys
sys.stdin = open('1221.txt', 'r')

T = int(input())
ztn = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for num in range(1,T+1):
    case = input()
    numbers = input().split()
    result = []
    for j in ztn:
        result += [j]*numbers.count(j)
    print('#{}'.format(num))
    print(' '.join(result))


# a=[]
# b=2
# a += [b]*2
# print(a)




