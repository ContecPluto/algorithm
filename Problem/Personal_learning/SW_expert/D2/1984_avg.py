import sys;sys.stdin = open('1984.txt','r')

T = int(input())
for tc in range(1, T+1):
    print('#{} {}'.format(tc, round(sum(sorted(list(map(int, input().split())))[1:9])/8)))