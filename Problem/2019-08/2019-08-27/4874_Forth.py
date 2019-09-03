import sys; sys.stdin = open('4874.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    calculate = input().split()
    stack = []
    for x in calculate:
        if x.isdecimal():
            stack.append(x)
        else:
            if x == '.':
                if len(stack) == 1:
                    print('#{} {}'.format(tc, int(stack[0])))
                    break
                else:
                    print('#{} error'.format(tc))
                    break
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            popword1 = int(stack.pop())
            popword2 = int(stack.pop())
            # print(x, stack, popword1, popword2)
            if x == '+':
                stack.append(popword2 + popword1)
            elif x == '*':
                stack.append(popword2 * popword1)
            elif x == '-':
                stack.append(popword2 - popword1)
            elif x == '/':
                stack.append(popword2 / popword1)

