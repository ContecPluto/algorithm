def fibo(n):
    global cnt
    cnt+= 1
    if n>=2 and memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

cnt = 0
N = int(input())
memo= [-1]* (N+1)
memo[0] = 0
memo[1] = 1
print('피보나치 결과', fibo(N))
print('호출횟수', cnt)
print(memo)

# memo에 작은것부터 저장해가며 계산하는 방식
# for 루프가 한번 돌 떄마다 앞에서 구해 저장해 놓은 피보나치 수 2개를 배열에 가져다 더하면 된다.
# (중복 호출이 야기한 비효율을 제거한다)