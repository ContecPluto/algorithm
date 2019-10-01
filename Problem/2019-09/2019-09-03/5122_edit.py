import sys; sys.stdin = open('5122.txt', 'r')


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

def edit(pre, data): #pre 다음에 데이터 삽입, 가운데 노드로 삽입하는 알고리즘
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link.link)

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

T=int(input())
for tc in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    Head = None

    for i in seq:
        addtoLast(i)

    for i in range(M):
        check = Head
        ed = list(map(str, input().split()))
        # print(ed)
        if ed[0] == 'I':
            for k in range(int(ed[1])-1):
                check = check.link
            add(check, ed[2])
        if ed[0] == 'D':
            for k in range(int(ed[1])-1):
                check = check.link
            delete(check)
        if ed[0] == 'C':
            for k in range(int(ed[1]) - 1):
                check = check.link
            edit(check, ed[2])

    check = Head
    for i in range(L):
        if check.link == None:
            print('#{} -1'.format(tc))
            break
        check = check.link
    else:
        print('#{} {}'.format(tc, check.data))








    # print(N)
    # while Head.link != None:
    #     print(Head.data, end=' -> ')
    #     Head = Head.link
    # print(Head.data)

