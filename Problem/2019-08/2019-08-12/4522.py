import sys
sys.stdin = open('4522.txt','r')

T = int(input())
for num in range(1, T+1):
    words = input()
    for i in range(len(words)):
        if words[i] == words[len(words) - i - 1] or words[i]=='?' or words[len(words) - i - 1] == '?' : continue
        else:
            print('#{} Not exist'.format(num))
            break
    else: print('#{} Exist'.format(num))



