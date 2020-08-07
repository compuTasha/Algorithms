arr = [[0 for i in range(10)]for j in range(10)]
for i in range(10):
    temp = list(map(int, input().split()))
    for j in range(10):
        arr[i][j] = temp[j]
x = 1
y = 1
while(1):
    if arr[x][y]==2:
        arr[x][y]=9
        break

    if arr[x+1][y] == 1 and arr[x][y+1] == 1:#끝에 도달한 경우
        arr[x][y]=9
        break

    elif arr[x][y+1]==1:#오른쪽 막힌 경우
        arr[x][y]=9
        if arr[x+1][y]==1:
            break
        x=x+1

    elif arr[x+1][y]==1:#아래 막힌 경우
        arr[x][y]=9
        if arr[x][y+1]==1:
            break
        y=y+1
    else:#오른쪽으로 이동
        arr[x][y]=9
        y=y+1
   
for i in range(10):
    for j in range(10):
        print("%d "%(arr[i][j]), end="")
    print()
