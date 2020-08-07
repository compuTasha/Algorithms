cnt=int(input())
arr=list(map(int,input().split()))
min=1000

for i in range(cnt):
    if min>=arr[i]:
        min=arr[i]
print(min)