num = int(input())
if num<0:
    print("minus")
    if num%2==0:
        print("even")
    else:
        print("odd")
else:
    print("plus")
    if num%2==0:
        print("even")
    else:
        print("odd")
