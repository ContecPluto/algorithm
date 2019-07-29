#버블 정렬 1차
array = [55, 7, 78, 12, 42]
n = len(array)
for i in range(n-1):
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]

print(array)

#버블 정렬 2차
for i in range(n-2):
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]

print(array)
    
#거품 정렬 (줄이고 모든 값이 정렬되도록 함)
array = [55, 7, 78, 12, 42]
n = len(array)
for j in range(n-1 , 0, -1):
    for i in range(j):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

print(array)


#선택 정렬
#최소가 array[0]라 가정 햇을때 하나 하나씩 비교하여 크면 버리고 작으면 min_array로 바꿔준다.
array = [55, 7, 78, 12, 42]
min_array = array[0]
for i in  range(1, len(array)):
    if array[i] < min_array:
        min_array = array[i]

print(min_array)

#최솟값 찾기

# 최솟값을 제일 앞에 두고자한다.
array = [55, 7, 78, 12, 42]
min_array = 0
for i in range(1, len(array)):
    if array[i] < array[min_array]:
        min_array = i

print(min_array, array)

array[0], array[min_array] = array[min_array], array[0]
print(array)

for i in range(min_array + 2, len(array)):
    if array[i] < array[min_array]:
        min_array = i

print(min_array, array)

array[1], array[min_array] = array[min_array], array[1]
print(array)

###### 위의 코드를 줄이면 밑의 코드와 같이 된다.

array = [55, 7, 78, 12, 42]
for j in range(len(array)-1):
    min_array = j
    for i in  range(j + 1, len(array)):
        if array[i] < array[min_array]:
            min_array = i
    array[j], array[min_array] = array[min_array], array[j]
print(array)


# 카운팅 정렬
data = [0, 3, 1, 3, 1, 2, 4, 1]
counts = [0] * 5       #최댓값 = 4
for val in data:
    counts[val] += 1
print(counts)

sorted_data = []
for i in range(len(counts)):
    for j in range(counts[i]):
        sorted_data.append(i)
print(sorted_data)


# 이를 이용한 누적빈도수 

data = [0, 3, 1, 3, 1, 2, 4, 1]
counts = [0] * 5       #최댓값 = 4

for val in data:
    counts[val] += 1
print(counts)
for i in range(1, len(counts)):
    counts[i] += counts[i-1]
print(counts)
