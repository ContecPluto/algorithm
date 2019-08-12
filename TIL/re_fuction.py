#재귀 함수 -> 자기 자신을 호출하는 함수
#재귀 호출 --> 재귀적 정의 (점화식) 구현하기 위해
#for, while을 사용하지 않고적 작업을 할 수 있다.

# def printhello(i, n):
#     if i == n:
#         print('----------------')
#         return
#     else:
#         print(i, '> Hello')
#         printhello(i + 1, n)

cnt = 0
def printhello(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
    printhello(i + 1, n)
    printhello(i + 1, n)



printhello(0, 3)
print(cnt)

# for i in range(3):
#     print('Hello')




#그래프의 깊이 우선 탐색, 백트래킹