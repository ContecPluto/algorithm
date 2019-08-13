import sys
sys.stdin = open('4579.txt','r')

T = int(input())
for num in range(1, T+1):
    words = input()
    for x in range(len(words)):
        if words[x] == '*' or words[len(words)-1-x] == '*':
            print('#{} Exist'.format(num))
            break
        if words[x] == words[len(words)-1-x]: continue
        else:
            print('#{} Not exist'.format(num))
            break
    else:
        print('#{} Exist'.format(num))




