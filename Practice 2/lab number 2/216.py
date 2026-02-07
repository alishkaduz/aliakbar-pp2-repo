n = int(input())
a = list(map(int, input().split()))
alr = set()
for i in range(n):
    if a[i] not in alr:
        print('YES')
        alr.add(a[i])
    else:
        print('NO')