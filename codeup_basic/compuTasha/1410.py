bracket = input()
open = 0; close = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        open += 1
    else:
        close += 1

print(open, close)