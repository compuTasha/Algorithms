char_end = input()
char = 'a'

while True:
    print(char)
    if char == char_end:
        break
    char = chr(ord(char) + 1)