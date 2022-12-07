# https://www.acmicpc.net/problem/2525

# 현재 시각
hour, minute = map(int, input().split(" "))

# 필요 시간
time = int(input())

minute = minute + time
hour =  hour + (minute // 60)

print(f"{hour % 24} {minute % 60}")