import sys
sys.stdin = open('4865.txt', 'r')

T = int(input())
for num in range(1, T+1):
    str1 = input()
    str2 = input()
    count = 0

    for word in str1:
        count = max(str2.count(word), count)
    print('#{} {}'.format(num, count))