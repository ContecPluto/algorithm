import sys; sys.stdin = open('5120.txt', 'r')

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data): #첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)

def addtoLast(data): #마지막 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을 때 까지
            p = p.link
        p.link = Node(data, None)

def add(pre, data): #pre 다음에 데이터 삽입, 가운데 노드로 삽입하는 알고리즘
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    password = list(map(int, input().split()))
    Head = None

    for i in password:
        addtoLast(i)

    check = Head
    # for i in range(99):
    #     if check == None:
    #         check = Head
    #     else:
    #         check = check.link

    for j in range(K):
        total = 0
        for i in range(M):
            if j == 0 and i == 0:
                check = Head
            else:
                if check.link == None:
                    check = Head
                else:
                    check = check.link
            if i == M-2:
                if check.link ==None:
                    # print(Head.data, end=' ')
                    total += Head.data
                else:
                    # print(check.link.data,end=' ')
                    total += check.link.data
            if i == M-1:
                if check.link ==None:
                    # print(Head.data)
                    total += Head.data
                else:
                    # print(check.link.data)
                    total += check.link.data
        # print(check.data)
        add(check, total)
        N += 1

    if N > 10:
        check = Head
        for i in range(N-10):
            check = check.link

        result = []
        for _ in range(10):
            result.append(check.data)
            check = check.link
        print('#{} {}'.format(tc, ' '.join(map(str, reversed(result)))))
    else:
        check = Head
        result = []
        for _ in range(N):
            result.append(check.data)
            check = check.link
        print('#{} {}'.format(tc, ' '.join(map(str, reversed(result)))))


    # print(N)
    # while Head.link != None:
    #     print(Head.data, end=' -> ')
    #     Head = Head.link
    # print(Head.data)



