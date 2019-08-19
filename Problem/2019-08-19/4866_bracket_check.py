import sys
sys.stdin = open('4866.txt', 'r')

T = int(input())
top = -1

for i in range(1, T+1):
    words = list(input())
    check = []
    for j in range(len(words)):
        popword = words.pop(0)
        if popword == '(' or popword == '{':
            check.append(popword)
        elif popword == ')' or popword == '}':
            if not check:
                print('#{} 0'.format(i))
                break
            if popword == ')':
                if check.pop() != '(':
                    print('#{} 0'.format(i))
                    break
            if popword == '}':
                if check.pop() != '{':
                    print('#{} 0'.format(i))
                    break
    else:
        if not check:
            print('#{} 1'.format(i))
        else:
            print('#{} 0'.format(i))





