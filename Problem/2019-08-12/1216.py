import sys
sys.stdin = open('1216.txt','r')

for num in range(1, 11):
    N = input()
    words = [input() for _ in range(100)]
    result = 0

    for x in range(100):
        for y in range(100):
            for z in range(100-y):
                if 100-z-y > result:
                    for i in range((100-z-y)//2):
                        if words[x][y+i] != words[x][99-i-z]:break
                    else:
                        result = max(result, 100-z-y)
                    for i in range((100-z-y)//2):
                        if words[y+i][x] != words[99-i-z][x]:break
                    else:
                        result = max(result, 100-z-y)
                else:break
    print('#{} {}'.format(num, result))
