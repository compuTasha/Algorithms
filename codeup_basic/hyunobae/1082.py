num=int(input(),16)
a=num
num=format(num,'X')

for i in range(1,16):
    re=hex(i*a)[2:].upper()
    i=format(i,'X')
    print(num+"*"+i+"="+re)