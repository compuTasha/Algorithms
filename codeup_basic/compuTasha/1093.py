n = int(input())
num = list(map(int, input().split()))
arr = [0] * 23

for i in num:
    arr[i-1] += 1

for i in arr:
    print(i, end=" ")