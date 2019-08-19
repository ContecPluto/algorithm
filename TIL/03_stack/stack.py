# c-style

S = [0] * 10
top = -1

def push(item):
    global top
    # full 상태를 체크
    if top == 2: return
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

for i in range(3):
    push(i)

print(pop())
print(pop())
print(pop())

# python style
S = []
def push(item):
    S.append(item)
def pop(): #항상 empty 상태를 체크
    return S.pop()
def isEmpty():
    return  len(S) == 0
for i in range(3):
    push(i)
while not isEmpty():
    print(pop())