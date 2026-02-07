a=int(input())
c={}
for i in range(a):
    b=input().split()
    if b[0] in c:
        c[b[0]]+=int(b[1])
    else:
        c[b[0]]=int(b[1])
for key in sorted(c.keys()):
    print(key, c[key])