# def factorial(n):   #매개변수 - 문제(크기)를 나타내는 값
#                     # 반환값 - n!의 값(문제의 해)
#     if n == 0 or n == 1:    #기저 사례
#         return 1    #재귀 호출 하지않고 종료
#     else:       #재귀호출
#         return factorial(n - 1) * n
# print(factorial(5))

# def fibonacci(n):     #n번쨰 피보나치 수를 반환
#     if n == 1 or n == 0:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# memo = [-1] * 100
# def fibonacci(n):     #n번쨰 피보나치 수를 반환
#     memo[0], memo[1] = 0, 1
#     if n == 1 or n == 0:
#         return n
#     if memo[n] != -1:
#         return memo[n]
#     else:
#         memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return memo[n]

memo = [-1] * 100
def fibonacci(n):     #n번쨰 피보나치 수를 반환
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]




print('시작')
print(fibonacci(30))
print('끝')