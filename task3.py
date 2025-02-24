# 1. Print the first 10 terms of the Fibanocci series using a For loop:

terms =int(input("Enter a number"))
num1 = 0
num2 = 1
print(num1, num2, end=" ")  
for i in range(2, terms):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3

# 2. Check if a given number is a prime number using a For loop:

num1 = int(input("Enter a number to check prime or not"))
flag = True
for i in range(2, num1):
    if num1 % i == 0:
        print(num1, "is not a Prime Number")
        flag = False
        break

if flag:
    print(num1, "is a Prime Number")

# 3. Write a Program to calculate the factorial of a number using a For Loop:

num = int(input("Enter a number to calculate the factorial:"))
res = 1
while num > 1:
    res = res * num
    num -= 1
print("The factorial is:", res)

# 4. Print all numbers from 1 to 100 that are divisible by 3 and 5 using a For Loop:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

# 5. Implement a menu - driven program when the user can choose to:
#    1. Find the square of a number
#    2. Find the cube of a number
#    3. Exit

num = int(input("Enter a Number"))
choice  = int(input("Enter a number from 1 to 3"))
while True:
    if choice == 1:
        print("The square of", num, "is:",num ** 2)
        False
        break
    elif choice == 2:
        print("The cube of", num, "is:", num ** 3)
        False
        break
    elif choice == 3:
        False
        break
    else:
        print("Enter the choice from 1 to 3 only")
        break