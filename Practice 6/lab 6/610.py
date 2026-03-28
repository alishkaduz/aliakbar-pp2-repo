n = int(input())
lst1 = list(map(int, input().split()))
cnt = sum(map(bool, lst1))

print(cnt)