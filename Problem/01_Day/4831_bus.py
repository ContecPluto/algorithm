import sys
sys.stdin = open('4831.txt', 'r')
T = int(input())

for num in range(T):
    K, N, M = list(map(int, input().split()))
    charger = list(map(int, input().split()))
    count = 0
    result = []
    #범위를 부여합니다.
    for number in range(N+1):
        for i in range(count, count + K + 1):
            #count만큼 진행을 하였을때 마지막에 도착한 충전소만을 리스트에 추가합니다.
            if i in charger and count + K < N:
                count = i
        result.append(count)

    #도착하지못한 배열에 0을 할당하기 위해 빈 리스트로 바꿔줄것입니다.
    for i in range(0, len(result)-1):
        if result[i] == result[i+1]:
            if result[i] + K < N:
                result = []
                break

    #셋으로 변환하여 중복값을 없애고 길이로서 몇번을 충전소에 들렸는지 확인합니다.
    print(result)
    result = len(set(result))



    print('#{} {}'.format(num+1, result))

