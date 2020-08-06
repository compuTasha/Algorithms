h,b,c,s=map(int,input().split())
result=h*b*c*s

result=result/8
result=result/1024
result=result/1024

print("%.1lf MB"%result)