numbers = '2+3*4/5'
stack = []
top= -1
for i in numbers:
    if i.isdigit() == True:
        print(i, end=' ')
    elif i == '+' or i == '-' or i == '*' or i == '/':
        top += 1
        stack.append(i)

for i in range(0, top+1):
    print(stack.pop(), end=' ')


