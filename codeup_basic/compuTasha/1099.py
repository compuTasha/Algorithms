arr = [[0 for col in range(10)] for row in range(10)]
for i in range(10):
    temp = list(map(int, input().split()))
    for j in range(10):
        arr[i][j] = temp[j]
x = 1; y = 1

while True:
    if arr[x][y] == 2:
        arr[x][y] = 9 
        break
    elif arr[x][y+1] != 1:
        arr[x][y] = 9 
        y += 1
    elif arr[x+1][y] != 1:
        arr[x][y] = 9 
        x += 1
    else:
        arr[x][y] = 9 
        break

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()