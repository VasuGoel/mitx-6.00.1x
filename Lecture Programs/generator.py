def genTest():
    print('Block of code before first yield statement')
    yield 1
    print('Block of code after first yield statement and before second yield statement')
    yield 2
    print('Block of code after all yield statements')


# foo = genTest   returns <function gen at 0x101faf400>
foo = genTest()   # returns <generator object gen at 0x101f9f408>

print(foo.__next__())
print()
print(foo.__next__())

print('\n')

for f in foo:
    print(f)


# **OUTPUT**

# Block of code before first yield statement
# 1

# Block of code after first yield statement and before second yield statement
# 2
#
#
# Block of code after all yield statements
