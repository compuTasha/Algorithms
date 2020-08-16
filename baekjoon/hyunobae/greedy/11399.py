num=int(input())
line=list(map(int,input().split()))
time=0

for i in range(num):
    for j in range(i+1,num):
        if line[i]>line[j]:
            line[i],line[j]=line[j],line[i]

cnt=1

for i in range(num):
    for j in range(cnt):
        if cnt==j:
            break
        time=time+line[j]
    cnt+=1

print(time)