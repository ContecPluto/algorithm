import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for num in range(1,T+1):
    N, M = list(map(int, input().split()))
    fly = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    result = 0

    for fly_x in range(len(fly)):
        if fly_x + M > N: break  #에러 방지용 ex) Testcase1 을 기준으로 마지막에서 2개를 새려고하면 에러가남.
        for fly_y in range(len(fly)):
            if fly_y + M  > N: break #에러 방지용2
            for x in range(fly_x, fly_x + M): #파리채 크기
                for y in range(fly_y, fly_y + M):
                    total += fly[x][y]
            result = max(total, result)
            total = 0
    print('#{} {}'.format(num, result))


