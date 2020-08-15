n = int(input())
num = list(map(int, input().split()))


for i in range(n):
    for j in num:
        print(j, end=' ')
    print()
    num.append(num[0])
    num.remove(num[0])