def solution(N, number):
    answer = -1
    dp = [{N}, {N}]
    for idx in range(1, 9):
        dp.append(set())
        dp[idx].add(int(str(N) * idx))
        for x_idx in range(1, idx//2+1):
            for i in dp[x_idx]:
                for j in dp[idx-x_idx]:
                    dp[idx].add(i+j)
                    if i - j > 0:
                        dp[idx].add(i-j)
                    if j - i > 0:
                        dp[idx].add(j-i)
                    dp[idx].add(i*j)
                    if j:
                        dp[idx].add(i//j)
                    if i:
                        dp[idx].add(j//i)

        for num in dp[idx]:
            if num == number:
                return idx
    return answer

print(solution(5, 55*55))