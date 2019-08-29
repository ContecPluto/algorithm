import sys; sys.stdin = open('5356.txt', 'r')

T = int(input())
for tc in range(1, 3):
    word = [input() for _ in range(5)]
     
    # print('#{}'.format(tc), end=' ')
    for x in range(15):
        for y in range(5):
            # print('인덱스',word[y][x], end=' ')
            # print('슬라이싱',word[y][x:x+1])
            # if word[y][x:x+1]:        
            print(word[y][x:x+1], end='')
    print()
