#請算出 (1+2)*(3²)+5 的值

print("(1+2)*(3²)+5 的值")
def 加法(x,y):
    return x + y
def 乘法(a,b):
    return a * b
x = 1
y = 2
a = 3
b = 3

加法過程 = 加法(x,y)
乘法過程 = 乘法(a,b)

print(f"結果為: {乘法(加法過程, 乘法過程) + 5}")


