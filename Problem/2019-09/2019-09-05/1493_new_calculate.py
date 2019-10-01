import sys; sys.stdin = open('1493.txt','r')

def find(data):
    result = 0
    for x in range(1, 10001):
        y = 1
        while x != 0:
            # print(y, x)
            result += 1
            if result == data:
                return x, y
            x -= 1
            y += 1
#
def check(data):
    result = 0
    for x in range(1, 10001):
        y = 1
        while x != 0:
            # print(y, x)
            result += 1
            if [x, y] == data:
                return result
            x -= 1
            y += 1


T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))
    x, y = find(p)
    z, w = find(q)
    print('#{} {}'.format(tc, check([x + z, y + w])))



