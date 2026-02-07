n = int(input())
a = list(map(int, input().split()))
count = 0
most_frequent = a[0]
for i in range(n):
    a.count(a[i])
    if a.count(a[i]) > count:
        count = a.count(a[i])
        most_frequent = a[i]
    elif a.count(a[i]) == count and a[i] != most_frequent:
        most_frequent = min(most_frequent, a[i])
    
print(most_frequent)