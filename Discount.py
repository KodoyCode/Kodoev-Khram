a = 2000
b = 4000
c = 12000
d = int(input("How much bread do you want?: "))
e = int(input("How much milk do you want?: "))
f = int(input("How much eggs do you want?: "))

print("Without discount")
print("Bread:")
print(a*d)
print("Milk:")
print(b*e)
print("Eggs:")
print(c*f)

print("With discount")
print("Bread:")
print(a/100*90*d)
print("Milk:")
print(b/100*88*e)
print("Eggs:")
print(c/100*87*f)