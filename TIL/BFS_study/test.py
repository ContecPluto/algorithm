def solution(n):
    answer = 0
    for i in range(1,n+1):
        total = 0
        for j in range(i, n+1):
            total += j
            if total == 15:
                answer +=1
                break
            elif total > 15:
                break
    return answer

print(solution(15))