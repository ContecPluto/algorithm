import sys; sys.stdin = open('5356.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     word = [input() for _ in range(5)]
#
#     print('#{}'.format(tc), end=' ')
#     for x in range(15):
#         for y in range(5):
#             print(word[y][x:x+1], end='')
#     print()

T = int(input())
for tc in range(1, T+1):
    word = [input() for _ in range(5)]
    l = [len(i) for i in word]
    ml = max(l)

    temp = ''
    for i in range(ml):
        for j in range(5):
            if l[j] > i:
                temp += word[j][i]
    print(temp)

