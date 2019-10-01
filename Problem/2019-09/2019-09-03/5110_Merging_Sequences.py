import sys; sys.stdin = open('5110.txt', 'r')

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoLast(data): #마지막 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을 때 까지
            p = p.link
        p.link = Node(data, None)

def addtoFirst(data): #첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)

def add(pre, data): #pre 다음에 데이터 삽입, 가운데 노드로 삽입하는 알고리즘
    if pre == None:
        return 'error'
    else:
        pre.link = Node(data, pre.link)

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    Head = None

    for j in range(N):
        sequence = list(map(int, input().split()))
        if not Head:
            for i in sequence:
                addtoLast(i)
        else:
            check_link = Head
            while check_link.link != None:
                if Head.data > sequence[0]:
                    sequence.reverse()
                    for i in sequence:
                        addtoFirst(i)
                    break
                if check_link.link.data > sequence[0]:
                    for i in sequence:
                        add(check_link, i)
                        check_link = check_link.link
                    break
                check_link = check_link.link
            else:
                for i in sequence:
                    add(check_link, i)
                    check_link = check_link.link

    check = Head
    for i in range(N*M-10):
        check = check.link

    # while Head.link != None:
    #     print(Head.data, end=' -> ')
    #     Head = Head.link
    # print(Head.data)

    result = []
    for _ in range(10):
        result.append(check.data)
        check = check.link
    print('#{} {}'.format(tc, ' '.join(map(str, reversed(result)))))


