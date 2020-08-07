n = int(input())
num = list(map(int, input().split()))
num.reverse()

for i in num:
    print(i, end=' ')