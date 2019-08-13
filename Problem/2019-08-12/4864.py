import sys
sys.stdin = open('4864.txt','r')

T=int(input())
for num in range(T):
    str1 = input()
    str2 = input()
    for i in range(len(str2)):
        if str2[i] == str1[0]:
            if str2[i:i+len(str1)] == str1:
                print('1')
                break
    else:
        print('0')
