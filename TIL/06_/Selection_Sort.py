arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]

def getMin(s, e):  #최소값 구하기 [큰 문제]
    if s==e:  #기저 사례
        # print(arr[e])
        return arr[s] #가장 작은 문제:
    else:
        mid = (s + e)//2
        # ret = getMin(s, e-1)        #매개변수 => 문제의크기, 반환값 => 문제의 해 [더 작은 문제]
        # print(arr[e])
        l = getMin(s, mid)
        r = getMin(mid +1, e)
        return min(l, r)


print(getMin(0, len(arr)-1))