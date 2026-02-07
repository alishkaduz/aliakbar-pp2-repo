n = int(input())
x = range(0, 32)
for i in x:
    if n == 2**i:
        print("YES")
        break
else:
    print("NO")