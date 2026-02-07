n = int(input())
arr = input().split()
max = int(arr[0])
for i in range(1, n):
    if int(arr[i]) > max:
        max = int(arr[i])

print(max)