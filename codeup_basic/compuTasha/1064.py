a, b, c = map(int, input().split())
min = a if a < b else b
min = c if c < min else min
print(min)