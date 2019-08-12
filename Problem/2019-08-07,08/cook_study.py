arr = [1,2,3,4,5,6]
N=6

for set in range(1 << 5):
    A, B = [], []
    for i in range(N):
        if set & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)