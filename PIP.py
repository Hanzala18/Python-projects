x = 50
y = 60
z = 95.26
txt = "he got {} in maths, {} in science  {:.3f} in chem"
print(txt.format(x, y, z))

# x = 50
# y = 60
# z = 95.26
# txt = "he got {0} in maths, {:.2f} in science  {:.3f} in chem"
# print(txt.format(x, y, z))
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

k = "my name is {name}"
print(k.format(name="Hanzala"))
