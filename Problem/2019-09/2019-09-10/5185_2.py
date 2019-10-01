import sys; sys.stdin = open('5185.txt', 'r')


num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
num2 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}


T = int(input())
for tc in range(1, T+1):
    N,x = input().split()

    result = []
    c = len(x) - 1
    for i in x:
        if not i.isdecimal():
            number = num.get(i)
            for j in range(3, -1, -1):
                if number >= (2**j):
                    number -= (2**j)
                    result.append('1')
                else:
                    result.append('0')
        else:
            number = int(i)
            for j in range(3, -1, -1):
                if number >= (2 ** j):
                    number -= (2 ** j)
                    result.append('1')
                else:
                    result.append('0')
    print('#{} {}'.format(tc, ''.join(result)))