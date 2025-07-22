name="happy"

print(len(name))

a="HELLO"
print(a.lower())

b="hello"
print(b.upper())

c="hello world"
print(c.capitalize())

d=" hello   "
print(d.strip())

e="Hello world"
print(e.replace("world","python"))

f="apple,banana,grape"
print(f.split(","))

items=["apple","banana","grape"]
print(",".join(items))

g="Hello world"
print(g.find("world"))

h="Hello world"
print(h.startswith("Hello"))
print(h.endswith("world"))

i="Hello"
print(i.isalpha())

j="123456"
print(j.isdigit())

k=("Hello123")
print(k.isalnum())

l="banana"
print(l.count("n"))

character="John"
age=30
print("my name is {} and I am {}years old.".format(character,age))