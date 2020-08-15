# 함수는 항상 메인 스크립트 위에
'''
def add(a, b):
    c = a+b
    print(c)

add(3, 2)
'''

def add(a, b):
    c = a+b
    return c

x = add(3, 2)
print(x)