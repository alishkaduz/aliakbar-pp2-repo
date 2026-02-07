a=int(input())
b=list()
c=set()
for i in range(a):
    b.append(input())
for i in b:    c.add(i)
c=list(c)
c.sort()
for i in c:
    ind=b.index(i)+1
    print(i, ind)