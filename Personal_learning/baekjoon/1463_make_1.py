import sys

def dp(n):
    if arr.get(n) != None:
        return arr[n]
    else:
        if n % 6 == 0:
            arr[n] = min(dp(n//3), dp(n//2)) + 1
        elif n % 3 == 0:
            arr[n] = min(dp(n//3), dp(n-1)) + 1
        elif n % 2 == 0:
            arr[n] = min(dp(n//2), dp(n-1)) + 1
        else:
            arr[n] = dp(n-1) + 1
        return arr[n]

N = int(sys.stdin.readline())
arr = {0: 0, 1:0, 2:1, 3:1}
print(dp(N))

# 초기에 짠 DP
# 처음 한번만 작동할 때는 정상 작동하나 메모이제이션 기능이 생략되어 시간과 메모리를 많이 사용한다.
# 위의 함수식을 사용한다면
# 입력값이 N = 5 => N => 7 과 같이 N이 주어진다면
# 메모이제이션으로 5 => 7 까지만 작동하면 된다.
# 아래 코드의 같은경우 2 => 5 까지 작동 2 => 7 까지 작동하므로 비효율적이다.

# for i in range(2, N + 1):
#     if i % 6 == 0:
#         arr[i] = min(arr[i//3], arr[i//2]) + 1
#     elif i % 3 == 0:
#         arr[i] = min(arr[i//3], arr[i-1]) + 1
#     elif i % 2 == 0:
#         arr[i] = min(arr[i//2], arr[i-1]) + 1
#     else:
#         arr[i] = arr[i-1] + 1