n = int(input())
a = []
for i in range(1, n+1):
    a.append(i)

for i in range(n-1):
    temp = int(input())
    a.remove(temp)

print(a[0])