a,m,d,n=map(int,input().split())
result=a

for i in range(1,n):
    result=result*m
    result=result+d
print(result)