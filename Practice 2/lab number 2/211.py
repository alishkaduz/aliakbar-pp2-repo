# n = int(input())
# l = int(input())
# r = int(input())
inp = list(map(int, input().split()))
a = list(map(int, input().split()))
b = a[inp[1]-1:inp[2]]
b.reverse()
print(*a[:inp[1]-1], *b, *a[inp[2]:])