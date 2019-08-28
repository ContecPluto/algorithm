arr ='ABC'
bits = [0] * len(arr)
def subset(k, n): #k: 현재 노드의 높이, n:단말노드의 높이
    if k == n: #하나의 부분집합 생성
        for i in range(n):
            if bits[i]: print(arr[i], end=' ')
        print()
    else:
        bits[k] = 1; subset(k + 1, n) #arr[k] 포함
        bits[k] = 0; subset(k + 1, n)#arr[k] 포함하지않음

subset(0, 3)
#0 : 초기, 어떤선택도 하지않았따.
#3 : 선택한 수