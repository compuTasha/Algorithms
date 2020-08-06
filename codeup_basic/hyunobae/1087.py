num = int(input())
sum=0

for i in range(num+1):
    if(sum>=num):
        break
    else:
        sum=sum+i

print(sum)