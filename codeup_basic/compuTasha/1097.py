arr = [[0 for col in range(19)] for row in range(19)]
for i in range(19):
    temp = list(map(int, input().split()))
    for j in range(19):
        arr[i][j] = temp[j]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if arr[x-1][j] == 0:
            arr[x-1][j] = 1
        else: 
            arr[x-1][j] = 0
    for j in range(19):
        if arr[j][y-1] == 0:
            arr[j][y-1] = 1
        else:
             arr[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()