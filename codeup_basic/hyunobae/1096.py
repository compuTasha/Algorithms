num = int(input())
arr=[[0 for i in range(19)]for j in range(19)]
for i in range(num):
    x,y=map(int,input().split())
    arr[x-1][y-1]=1

for i in range(19):
    for j in range(19):
        print("%d "%arr[i][j], end="")
    print()