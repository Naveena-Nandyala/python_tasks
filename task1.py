# Assignment:

# How to declare different types of data types
# Operators
# Conditional Statements - if and else statements, elif
# Loops - while, for, jump statements - break, continue
# Functions - Declaring a function and call a function, return statement usage
# Inbuilt Functions - Atleast the most famous once - string and list


# 1) Data Types in Python:

# 1. string:
a="Python"
print(a)
print(type(a))

str="language"
print(str)
print(type(str))

# 2. int:
b=1
print(b)
print(type(b))

i =100
print(i)
print(type(i))

# 3. float
c=20.5
print(c)
print(type(c))

f=23.5
print(f)
print(type(f))

# 4. complex
d=2+3j
print(d)
print(type(d))

complex = 3 + 5j
print(complex)
print(type(complex))

# 5. list
x = [12, "python", 20.5]
print(x)
print(type(x))

li = [10, 20, 30]
print(li)
print(type(li))

# 6. set
y={"apple", "banana", "orange"}
print(y)
print(type(y))

s={12, 3, "banana"}
print(s)
print(type(s))

# 7. tuple
z= (12, "language", 35.77, "langauge")
print(z)
print(type(z))

t = ("Python", "java", "javascript")
print(t)
print(type(t))

# 8. range
r= range(10)
print(r)
print(type(r))

y=range(100)
print(y)
print(type(y))

# 9. Dictionary
dict = {"name":"Naveena", "age": 24, "qualification":"MCA"}
print(dict)
print(type(dict))

d = {"name": "lakshmi", "qualification":"Btech"}
print(d)
print(type(d))

# 10. Boolean 
bool = True
print(bool)
print(type(bool))

bool = False
print(bool)
print(type(bool))

# --------------------------------------------------------------------------------

# 2) Operators in Python

# 1. Arthimetic Operators:
print(10 + 5)
print(10 - 5)
print(12 * 5)
print(16 / 4)
print(20 % 3)
print(12 ** 2)
print(16 // 4)

# 2. Assignment Operators:
x = 5
print(x)
y= 5
y += 10
print(y)
z = 15
z -= 5
print(z)
a = 15
a *= 5
print(a)
b = 15
b /= 5
print(b)
b = 15
b //= 5
print(b)

# 3. Comparison Operators
a = 10
b = 10
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 4. Logical Operators
x = 5
print(x > 3 and x < 10)
print(x > 2 or x <4)
print(not(x > 3 and x < 10))

# 5. Bitwise Operators
print(6 & 3)
print( 5 | 4)
print(5 ^ 7)
print(~5)
print(3 << 2)
print(8 >> 2)
# ----------------------------------------------------------------------------------------

# 3. Conditional Statements in Python:

# 1. If Statement:

a = 33
b = 200
if b > a:
    print("b is greater than a")

age = 18
if age >= 18:
    print("Major")

# 2. Elif Statement

x = 20
y = 30
if y > x:
    print("y is greater")
elif a == b:
    print("Both are equal")

# 3. Else Statement:

age = 25
if age < 18:
    print("Not eligible to vote")
elif age == 18:
    print("Ypu are eligible to apply for voter card")
else:
    print("You are eligible to vote")

# --------------------------------------------------------------------------------------

# 4. Loop Statements in Python:

# 1. While Loop:
i = 1
while(i <= 10):
    print(i)
    i = i + 1

# 2. For Loop:

for i in range(2, 3):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)

# Jump Statements:
# break:
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 20):
    if i == 13:
        continue
    print(i)

# pass:
for alphabet in "python":
    if alphabet == 'o':
        pass
    else:
        print(alphabet)

# ---------------------------------------------------------------------------------

# 5. Functions in Python:

firstName = "Naveena"
lastName = "Nandyala"
def name():
    print(firstName, lastName)

name()

def addition(a, b):
    print(a + b)

addition(100, 100)

age = 20
def func():
    return age

res = func()
print("The result is:", res)

# -------------------------------------------------------------------------------------------------

# 6. Inbulit Functions in Python:
# String Functions:
# 1) capitalize(): Uppercase the first letter in the string.
text ="python is a programming language"
x = text.capitalize()
print(x)

# 2) index(): 
txt = "Hello, welcome to my world"
y = txt.index("e")
print(y)

# list functions:
# 1) append():
a = [1, 2, 3]
a.append(4)
print(a)

# 2) count():
c = [1, 2, 3, 4, 5, 6, 7, 2, 3, 2, 5, 7, 2]
print(c.count(2))