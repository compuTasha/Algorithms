arr=[[0 for i in range(19)]for j in range(19)]
for i in range(19):
    temp=list(map(int,input().split()))
    for j in range(19):
        arr[i][j]= temp[j]
cnt=int(input())
for i in range(cnt):
    x,y=map(int,input().split())
    for j in range(19):
        if arr[x-1][j]==1:
            arr[x-1][j]=0

        elif arr[x-1][j]==0:
            arr[x-1][j]=1

    for j in range(19):
        if arr[j][y-1]==1:
            arr[j][y-1]=0
        elif arr[j][y-1]==0:
            arr[j][y-1]=1

for i in range(19):
    for j in range(19):
        print("%d "%arr[i][j], end="")
    print()
