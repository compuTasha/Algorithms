char=input()
char=ord(char)
start='a'
temp=ord(start)
while(chr(temp)!=chr(char+1)):
    print(chr(temp))
    temp=temp+1