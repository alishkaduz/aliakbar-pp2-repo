n = int(input())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)
for i in range(n):
    if a[i] == max_val:
        a[i] = min_val

print(*a)  

