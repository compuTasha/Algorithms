w, h, b = map(int, input().split())
result=w*h*b
result=result/8
result=result/1024
result=result/1024
print("%.2lf MB" %result)