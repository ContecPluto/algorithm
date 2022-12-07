# https://www.acmicpc.net/problem/10951

# 최대 입력 갯수가 주어지지 않은 문제
# while을 통해 반복 및 try except 사용
#try:
#    while True:
#        A, B = map(int, input().split(" "))
#        print(A + B)
#        #result.append(A + B)

#        #print(*result, sep="\n")
#except EOFError:
#    pass


# readlines() - 파일 내용 전체를 가져와 리스트로 반환합니다. 각 줄은 문자열 형태로 리스트의 요소로 저장됩니다.
# 해당 함수를 사용하여 해결이 가능하다.
import sys

lines = sys.stdin.readlines()
result = []
for line in lines:
    A, B = map(int, line.split())
    result.append(A + B)

print(*result, sep="\n")
