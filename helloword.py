from pers import Person

print("hello world")
x = input("Name:")
age = input("Age:")

print(age)
print(x)

p1 = Person(str(x), age)
p1.myfunc()
