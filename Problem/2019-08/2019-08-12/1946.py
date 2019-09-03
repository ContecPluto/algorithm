import sys
sys.stdin = open('1946.txt','r')

T = int(input())
for num in range(1, T+1):
    result=''
    N = int(input())

    for i in range(N):
        word = input().split()
        result += word[0]*int(word[1])
    #
    # print('#{}'.format(num))
    # for i in range(len(result[::10])):
    #     print(result[i*10:i*10+10:])


    # print('#{}'.format(num))
    # for i in range(len(result)):
    #     print(result[i], end='')
    #     if (i+1)%10==0:
    #         print()
    # print()
