N = int(input())
people = list(map(int, input().split()))
people.sort()
result = [people[0]] + [0] * (len(people) - 1)
for num in range(1, len(people)):
    result[num] = result[num-1] + people[num]
print(sum(result))