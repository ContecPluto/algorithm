import sys; sys.stdin = open('5432.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    sticks = input()
    count = 0
    result = 0

    for i in range(len(sticks)):
        if sticks[i] == '(':
            count += 1
            if sticks[i+1] == ')':
                count -= 1
                result += count 
            else:
                count -= 1
                result -= count
                count += 1
        if sticks[i] == ')' and sticks[i-1] != '(':
            result += count
            count -= 1
    print('#{} {}'.format(tc, result))
    

