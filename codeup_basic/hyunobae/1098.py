h,w=map(int,input().split())#h=세로 w=가로
arr=[[0 for i in range(w)]for j in range (h)]
n=int(input())

for i in range(n):
    l,d,x,y=map(int,input().split())#길이, 방향(0:가로), 막대시작위치
    if d==0:#가로
        for j in range(l):
            arr[x-1][y-1+j]=1
    elif d==1:
        for j in range(l):
            arr[x-1+j][y-1]=1

for i in range(h):
    for j in range(w):
        print("%d "%arr[i][j], end="")
    print()