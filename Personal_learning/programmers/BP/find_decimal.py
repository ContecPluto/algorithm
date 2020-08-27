def comb(numbers, arr, N, nums, visit):
    if arr:
        val = int("".join(arr))
        if val > 1:
            nums.add(val)
    for i in range(N):
        if visit[i] == False:
            arr.append(numbers[i])
            visit[i] = True
            comb(numbers, arr, N, nums, visit)
            visit[i] = False
            arr.pop()
    return nums


def solution(numbers):
    answer = 0
    # numbers = list(numbers)
    nums = set()
    nums = comb(numbers, [], len(numbers), set(), [False]*len(numbers))
    numbers = list(map(int, numbers))
    for num in nums:
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                break
        else:
            answer += 1
    return answer


print(solution("1231"))