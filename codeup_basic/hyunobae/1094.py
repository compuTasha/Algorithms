cnt = int(input())
save=list(map(int,input().split()))
save.reverse()
for i in range(0,cnt):
    print("%d "%save[i], end="")