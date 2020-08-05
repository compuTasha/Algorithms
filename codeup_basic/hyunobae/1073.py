import sys
num=list(map(int,input().split()))
for i in range(len(num)):
    if num[i]==0:
        sys.exit(0)
    else:
        print(num[i])
        i+=1