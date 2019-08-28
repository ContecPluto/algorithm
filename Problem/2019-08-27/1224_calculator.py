import sys; sys.stdin = open('1224.txt', 'r')
def isp(word):
    if word == '(':
        return 0
    elif word == '+':
        return 1
    elif word == '*':
        return 2
    elif word == '/':
        return 2

def icp(word):
    if word == '*':
        return 2
    if word == '+':
        return 1
    if word == '(':
        return 3
    if word == '/':
        return 2

for tc in range(1, 11):
    n = int(input())

    calculate = list(map(str, input()))
    stack = []
    stack2 = []
    for x in calculate:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if not stack2:
                stack2.append(x)
            else:
                if x != ')':
                    sp = isp(stack2[-1])
                    cp = icp(x)
                    if cp > sp:
                        stack2.append(x)
                    else:
                        stack.append(stack2.pop())
                        stack2.append(x)
                else:
                    while True:
                        check = stack2.pop()
                        if check == '(':
                            break
                        stack.append(check)


    stack2 = []
    for x in stack:
        if type(x) == int:
            stack2.append(x)
        else:
            if len(stack2) < 2:
                break
            popword1 = int(stack2.pop())
            popword2 = int(stack2.pop())
            if x == '+':
                stack2.append(popword2 + popword1)
            elif x == '*':
                stack2.append(popword2 * popword1)
    print('#{} {}'.format(tc, stack2[0]))
