def solution(numbers):
    numbers = sorted(numbers, reverse=True, key = lambda x : str(x)*3)
    return str(int("".join(map(str, numbers))))

# print(solution())
# print(solution([0,0,70]))
# print(solution([2,20,200]))
# print(solution([1,2,20,21, 21]))
# print(solution([10, 101]))
# print(solution([2357, 235785]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([2, 23, 20, 246, 9]))
# print(solution([500, 11, 12, 13]))
# print(solution([0, 0, 0, 0, 0, 0]))