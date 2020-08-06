cnt=int(input())
arr=list(map(int,input().split()))
relist=[0 for i in range(1,25)]

for i in range(cnt):
    relist[arr[i]]=relist[arr[i]]+1

for i in range(1,24):
    print("%d "%relist[i], end="")