n = int(input())
a = list()
b = set()
count = 0
for i in range(n):
    a.append(input())
for j in a:
    b.add(j)
for k in b:
    if a.count(k) == 3:
        count += 1


print(count)

