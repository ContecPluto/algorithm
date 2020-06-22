n = int(input())
star_list = list(range(1,20,2))

for star in range(n):
    print(' '*star, '*'*star_list[n-star-1])
for star in range(n-1, 0, -1):
    print(' '*(star-1), '*'*star_list[n-star])

