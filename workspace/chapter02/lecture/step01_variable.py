var1 = 'hello python'
print(var1)
print(type(var1))

var1 = 100
print(var1)
print(type(var1))

a = int(10.5)
b = int(20.42)
print(a+b)

a = float(10)
b = float(20)
print(a+b)

if a < 11:
    print("error")

print(10//3, 2**3)

num1 = 10
num2 = 20
print(num1 == num2)
print(not(num1 < 20 and num2 > 33))

num1 += 10
print(num1)

num3, num4 = 100, 50
num3, num4 = num4, num3
print(num3, num4)

lst = {1, 2, 3, 4, 5}
num3, *num4 = lst
print(num3, num4)
input()
