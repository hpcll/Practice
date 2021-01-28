list = [1,5,4,7,8]
n = len(list)
print(n)
for i in range(n):
    for j in range(0,n-i-1):
        if list[j] > list[j + 1]:
           list[j], list[j + 1] = list[j + 1], list[j]

print(list)
