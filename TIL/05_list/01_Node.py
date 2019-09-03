class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data): #첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)

def add(pre, data): #pre 다음에 데이터 삽입, 가운데 노드로 삽입하는 알고리즘
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data): #마지막 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을 때 까지
            p = p.link
        p.link = Node(data, None)

def delete(pre): #pre 다음 노드 삭제
    global Head
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link


data = [1,2,3,4]
Head = None


for i in range(len(data)):
    # addtoLast(data[i])
    addtoFirst(data[i])

check = Head
x=2
for i in range(20):
    if x < check.data:
        add(check, x)
        break
    else:
        check = check.link
# delete(Head.link)

print(Head.data)

# print(Head.data)
while Head.link != None:
    print(Head.data, end=' -> ')
    Head = Head.link
print(Head.data)
