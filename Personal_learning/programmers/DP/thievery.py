def solution(money):
    money = [0] + money
    N = len(money)
    dp = [0] * N
    dp2 = [0] * N
    dp[0] = money[1]
    dp[1] = money[1]
    dp[2] = money[2]
    dp2[2] = money[2]
    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]
        dp2[i] = max(dp2[i-2], dp2[i-3]) + money[i]   
    print(dp, dp2)
    return max(dp[-2], dp2[-1])


solution([1,2,3,1,5])