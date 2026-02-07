n = int(input())
a = list(map(int, input().split()))

max_value = a[0]
max_index = 0

for i in range(1, n):
    if a[i] > max_value:
        max_value = a[i]
        max_index = i

print(max_index + 1)








