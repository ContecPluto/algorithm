import sys
sys.stdin = open('1989.txt', 'r')

T = int(input())

for num in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print('#{} 1'.format(num))
    else:
        print('#{} 0'.format(num))

