# 11. 함수만들기
# 함수는 항상 메인 스크립트 위에

# def add(a, b):
#     c = a+b
#     print(c)

# add(3, 2)

# def add(a, b):
#     c = a+b
#     return c

# x = add(3, 2)
# print(x)

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]

# for i in a:
#     result = ifPrime(i)
#     print("%d : %s" %(i, result))

for x in a:
    if isPrime(x):
        print(x, end=' ')