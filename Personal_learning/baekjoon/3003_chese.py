# https://www.acmicpc.net/problem/3003

chese_piece = list(map(int, input().split(" ")))
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
## 체크용 체스 피스 리스트
check_piece = [1, 1, 2, 2, 2, 8]

for i in range(5):
    check_piece[i] -= chese_piece[i]

print(*check_piece, sep=" ")