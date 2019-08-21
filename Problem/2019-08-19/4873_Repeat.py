import sys; sys.stdin = open('4873.txt', 'r')

T = int(input())
for num in range(1, T+1):

    word = list(input())
    check = [word.pop()]
    top = -1
    for i in range(len(word)):
        popword = word.pop()
        if check:
            if popword == check[top]:
                check.pop()
            else:
                check.append(popword)
        else:
            check.append(popword)
    print('#{} {}'.format(num, len(check)))





