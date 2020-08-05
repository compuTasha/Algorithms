import sys
char = list(map(str,input().split()))

for i in range(len(char)):
    if char[i]=='q':
        print('q')
        sys.exit(0)
    else:
        print(char[i])