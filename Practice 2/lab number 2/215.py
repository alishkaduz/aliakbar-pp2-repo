n = int(input())
attendance = set()
for i in range(n):
    name = input()
    attendance.add(name)

print(len(attendance))