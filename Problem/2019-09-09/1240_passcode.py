import sys; sys.stdin = open('1240.txt','r')

passcode = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111',
            7: '0111011', 8: '0110111', 9: '0001011'}

def y_find():
    for x in range(N):
        for y in range(M):
            if text[x][y] == '1':
                return x

def find(x):
    for y in range(M - 6):
        for i in range(10):
            if text[x][y:y + 7] == passcode.get(i):
                return x, y

T = int(input())
for tc in range(1):
    N, M = list(map(int, input().split()))
    text = [input() for _ in range(N)]
    x = y_find()
    a, b = find(x)
    number = []
    while len(number) != 8:
        number = []
        for x in range(b, M, 7):
            for i in range(10):
                if text[a][x:x + 7] == passcode.get(i):
                    number.append(i)
                    break
            else:
                break
        b += 1
    print(number)
    even = 0
    odd = 0
    for i in range(8):
        if i % 2:
            odd += number[i]
        else:
            even += number[i]

    if (odd + (even * 3)) % 10 == 0:
        print('#{} {}'.format(tc, sum(number)))
    else:
        print('#{} 0'.format(tc))