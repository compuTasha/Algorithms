num = int(input(), 16)
num = int(num)

for i in range(1, 16):
    temp = num * i
    print("{0:X}*{1:X}={2:X}".format(num, i, temp))