import sys
sys.stdin = open('2007.txt', 'r')
T = int(input())

for num in range(T):
    my_str = input()
    word = ''
    for i in range(10):
        word += my_str[i]
        word2 = ''
        for j in range(len(word), len(word)+len(word)):
            word2 += my_str[j]
        if word == word2:
            # print(word)
            break
    print('#{} {}'.format(num+1, len(word)))

