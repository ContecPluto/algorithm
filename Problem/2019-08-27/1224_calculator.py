import sys; sys.stdin = open('1224.txt', 'r')

isp = ['(', '+', '*']
icp = ['+', '*', '(']



for tc in range(1):
    n = int(input())
    calculate = list(map(str, input()))
    # print(calculate)
    stack = []
    stack2 = ['(']
    for x in calculate:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if x == ')':
                for y in range(len(stack2)):
                    while stack2:
                        if isp.index(stack2[-1]) < isp.index(pop_stack):
                            break
                        if not stack2:
                            break
                        pop_stack = stack2.pop()
                        if pop_stack != '(':
                            stack.append(pop_stack)
                        else:
                            break
            else:
                stack2.append(x)
                if int(icp.index(stack2[len(stack2)-1])) < int(icp.index(x)):
                    stack(stack2.pop())




    print(stack)
    # stack2 = []
    # for x in stack:
    #
    #     if type(x) == int:
    #         stack2.append(x)
    #     else:
    #         if len(stack2) < 2:
    #             print('여기')
    #             break
    #         popword1 = int(stack2.pop())
    #         popword2 = int(stack2.pop())
    #         # print(x, stack, popword1, popword2)
    #         if x == '+':
    #             stack2.append(popword2 + popword1)
    #         elif x == '*':
    #             stack2.append(popword2 * popword1)
    # print(stack2)
